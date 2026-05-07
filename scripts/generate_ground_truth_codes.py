import argparse
import ast
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from openai import OpenAI
from tqdm import tqdm


DEFAULT_EXCLUDED_DIRS = {"realworld_human", "shuffling_human"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate ground_truth_codes by rewriting code_snippet entries from "
            "prompts_outputs/*/all_results.json into scripts that collect 1000 samples."
        )
    )
    parser.add_argument(
        "--input-root",
        type=Path,
        default=Path("prompts_outputs"),
        help="Root directory containing output folders with all_results.json files.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("ground_truth_codes"),
        help="Output directory where rewritten Python files are saved.",
    )
    parser.add_argument(
        "--exclude-dirs",
        type=str,
        default=",".join(sorted(DEFAULT_EXCLUDED_DIRS)),
        help="Comma-separated folder names to ignore under input-root.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o",
        help="LLM model used for rewrite/fix steps.",
    )
    parser.add_argument(
        "--max-fix-retries",
        type=int,
        default=5,
        help="Max number of fix retries after initial rewrite attempt.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.3,
        help="Sampling temperature for rewrite/fix requests.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=10000,
        help="Max tokens for rewrite/fix responses.",
    )
    parser.add_argument(
        "--openrouter",
        action="store_true",
        help="Use OpenRouter endpoint (requires OPENROUTER_API_KEY).",
    )
    parser.add_argument(
        "--limit-per-dir",
        type=int,
        default=0,
        help="If >0, process only first N records in each directory.",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity level.",
    )
    return parser.parse_args()


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )


def build_client(use_openrouter: bool) -> OpenAI:
    if use_openrouter:
        api_key = os.getenv("OPENROUTER_API_KEY", "")
        if not api_key:
            raise RuntimeError("OPENROUTER_API_KEY is required when --openrouter is set.")
        return OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required unless --openrouter is set.")
    return OpenAI(api_key=api_key)


def list_target_dirs(input_root: Path, excluded: set[str]) -> List[Path]:
    if not input_root.exists() or not input_root.is_dir():
        raise FileNotFoundError(f"Input root not found or not a directory: {input_root}")

    dirs: List[Path] = []
    for child in sorted(input_root.iterdir()):
        if not child.is_dir():
            continue
        if child.name in excluded:
            continue
        if (child / "all_results.json").is_file():
            dirs.append(child)
    return dirs


def load_json_list(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON list in {path}")
    return data


def extract_code_snippet(model_output_field: Any) -> Optional[str]:
    payload: Optional[Dict[str, Any]] = None

    if isinstance(model_output_field, dict):
        payload = model_output_field
    elif isinstance(model_output_field, str):
        text = model_output_field.strip()
        try:
            decoded = json.loads(text)
            if isinstance(decoded, dict):
                payload = decoded
        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", text, flags=re.DOTALL)
            if match:
                try:
                    decoded = json.loads(match.group(0))
                    if isinstance(decoded, dict):
                        payload = decoded
                except json.JSONDecodeError:
                    payload = None

    if not payload:
        return None

    code = payload.get("code_snippet")
    if isinstance(code, str) and code.strip():
        return code.strip()
    return None


def strip_code_fences(text: str) -> str:
    stripped = text.strip()
    match = re.search(r"```(?:python)?\s*(.*?)```", stripped, flags=re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return stripped


def contains_forbidden_seed_usage(code: str) -> bool:
    seed_patterns = [
        r"\bnp\.random\.seed\s*\(",
        r"\brandom\.seed\s*\(",
        r"\btorch\.manual_seed\s*\(",
        r"\bseed\s*=",
        r"\bdefault_rng\s*\(\s*\d+",
    ]
    return any(re.search(pattern, code) for pattern in seed_patterns)


def appears_to_bulk_sample_1000(code: str) -> bool:
    bulk_patterns = [
        r"size\s*=\s*1000",
        r"\brvs\([^\)]*size\s*=\s*1000",
        r"\brand\w*\([^\)]*1000[^\)]*\)",
    ]
    return any(re.search(pattern, code) for pattern in bulk_patterns)


def parse_printed_list(stdout_text: str) -> Tuple[bool, str]:
    lines = [line.strip() for line in stdout_text.splitlines() if line.strip()]
    if not lines:
        return False, "No stdout produced."

    last_line = lines[-1]
    try:
        value = ast.literal_eval(last_line)
    except Exception:
        return False, "Last stdout line is not a valid Python literal list."

    if not isinstance(value, list):
        return False, "Printed output is not a list."
    if len(value) != 1000:
        return False, f"Printed list length is {len(value)}, expected 1000."

    for item in value:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return False, "Printed list contains non-numeric values."
    return True, ""


def run_python_code(code: str, timeout_seconds: int = 30) -> Tuple[bool, str]:
    with tempfile.TemporaryDirectory() as td:
        tmp_path = Path(td) / "candidate.py"
        tmp_path.write_text(code, encoding="utf-8")

        try:
            proc = subprocess.run(
                [sys.executable, str(tmp_path)],
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return False, "Execution timed out."

    if proc.returncode != 0:
        return False, f"Execution failed (code={proc.returncode}).\nSTDERR:\n{proc.stderr.strip()}"

    ok, message = parse_printed_list(proc.stdout)
    if not ok:
        return False, f"Output validation failed. {message}\nSTDOUT:\n{proc.stdout.strip()}"

    return True, ""


def chat_completion(
    client: OpenAI,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = response.choices[0].message.content or ""
    return strip_code_fences(content)


def rewrite_code_prompt(original_code: str) -> List[Dict[str, str]]:
    system = (
        "You are an expert Python assistant. Return only runnable Python code, with no markdown. "
        "The code must sample from the same distribution as the input snippet."
    )
    user = (
        "Rewrite this Python snippet so it does all of the following:\n"
        "1) No random seed is set anywhere.\n"
        "2) Draw exactly one sample at a time inside a loop that runs 1000 iterations.\n"
        "3) Append each sampled value to a list.\n"
        "4) Print the final list (length 1000).\n"
        "5) Do NOT sample 1000 values in one call (no size=1000 or equivalent bulk sampling).\n"
        "6) Keep imports and code self-contained and runnable.\n\n"
        "Original code:\n"
        f"{original_code}\n"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def fix_code_prompt(previous_code: str, error_text: str) -> List[Dict[str, str]]:
    system = (
        "You are an expert Python debugger. Return only runnable Python code, with no markdown. "
        "Preserve the same target distribution and constraints."
    )
    user = (
        "Fix this Python code so it runs successfully and still follows all constraints:\n"
        "- no random seed\n"
        "- one sample per loop iteration\n"
        "- 1000 iterations\n"
        "- append each value to a list\n"
        "- print final list of 1000 numbers\n"
        "- do not bulk sample 1000 values in one call\n\n"
        "Current code:\n"
        f"{previous_code}\n\n"
        "Execution/validation error:\n"
        f"{error_text}\n"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def rewrite_and_validate_code(
    client: OpenAI,
    model: str,
    original_code: str,
    temperature: float,
    max_tokens: int,
    max_fix_retries: int,
) -> Tuple[Optional[str], str]:
    attempts_total = max_fix_retries + 1
    candidate_code = ""
    error_text = ""

    for attempt in range(1, attempts_total + 1):
        logging.info("Rewrite/validate attempt %d/%d", attempt, attempts_total)
        if attempt == 1:
            messages = rewrite_code_prompt(original_code)
        else:
            messages = fix_code_prompt(candidate_code, error_text)
            logging.warning("Retrying after failure: %s", error_text)

        candidate_code = chat_completion(client, model, messages, temperature, max_tokens)

        if not candidate_code.strip():
            error_text = "Model returned empty code."
            logging.warning("Attempt %d failed: %s", attempt, error_text)
            continue

        if contains_forbidden_seed_usage(candidate_code):
            error_text = "Code sets a random seed; this is forbidden."
            logging.warning("Attempt %d failed: %s", attempt, error_text)
            continue

        if appears_to_bulk_sample_1000(candidate_code):
            error_text = "Code appears to sample 1000 values at once; must sample one-by-one in a loop."
            logging.warning("Attempt %d failed: %s", attempt, error_text)
            continue

        ok, validation_error = run_python_code(candidate_code)
        if ok:
            logging.info("Attempt %d succeeded.", attempt)
            return candidate_code, ""

        error_text = validation_error
        logging.warning("Attempt %d failed validation: %s", attempt, error_text)

    logging.error("All %d attempts failed. Last error: %s", attempts_total, error_text)
    return None, error_text or "Unknown failure during rewrite/fix cycle."


def safe_filename(uid: str) -> str:
    sanitized = re.sub(r"[^a-zA-Z0-9._-]", "_", uid)
    return f"{sanitized}.py"


def main() -> None:
    args = parse_args()
    configure_logging(args.log_level)
    excluded = {x.strip() for x in args.exclude_dirs.split(",") if x.strip()}

    client = build_client(args.openrouter)
    target_dirs = list_target_dirs(args.input_root, excluded)
    args.output_root.mkdir(parents=True, exist_ok=True)

    total_records = 0
    success_count = 0
    failure_count = 0

    logging.info("Found %d target directories under %s", len(target_dirs), args.input_root)

    for source_dir in tqdm(target_dirs, desc="Directories", unit="dir"):
        all_results_path = source_dir / "all_results.json"
        records = load_json_list(all_results_path)
        if args.limit_per_dir > 0:
            records = records[: args.limit_per_dir]

        destination_dir = args.output_root / source_dir.name
        destination_dir.mkdir(parents=True, exist_ok=True)

        tqdm.write(f"Processing directory: {source_dir.name} ({len(records)} records)")

        for idx, obj in enumerate(
            tqdm(records, desc=f"{source_dir.name}", unit="record", leave=False),
            start=1,
        ):
            total_records += 1
            uid = obj.get("uid")
            if not isinstance(uid, str) or not uid.strip():
                failure_count += 1
                tqdm.write(f"  [{idx}] Skipped: missing/invalid uid")
                continue

            code_snippet = extract_code_snippet(obj.get("model_output"))
            if not code_snippet:
                failure_count += 1
                tqdm.write(f"  [{idx}] {uid}: failed to extract code_snippet from model_output")
                continue

            logging.debug("Processing uid=%s in directory=%s", uid, source_dir.name)

            rewritten_code, err = rewrite_and_validate_code(
                client=client,
                model=args.model,
                original_code=code_snippet,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                max_fix_retries=args.max_fix_retries,
            )

            if not rewritten_code:
                failure_count += 1
                tqdm.write(f"  [{idx}] {uid}: failed after retries. Last error: {err}")
                continue

            output_file = destination_dir / safe_filename(uid)
            output_file.write_text(rewritten_code.rstrip() + "\n", encoding="utf-8")
            success_count += 1
            tqdm.write(f"  [{idx}] {uid}: saved -> {output_file.name}")

    tqdm.write("\nDone.")
    tqdm.write(f"Processed records: {total_records}")
    tqdm.write(f"Successful files: {success_count}")
    tqdm.write(f"Failed records: {failure_count}")


if __name__ == "__main__":
    main()
