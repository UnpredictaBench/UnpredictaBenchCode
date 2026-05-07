from __future__ import annotations

import argparse
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from openai import OpenAI
from tqdm import tqdm

import realworld_mapping_helper
from runner_common import (
    build_call_params,
    build_client,
    create_chat_completion_with_retry,
    ensure_output_dir,
    ensure_boolean_optional_action,
    load_input_data,
    make_safe_id,
    parse_provider_order,
    save_summary,
    strip_json_fence,
)

ensure_boolean_optional_action(argparse)


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUESTIONS_FILE = REPO_ROOT / "prompts_human/realworld_human/questions.json"
DEFAULT_MAPPING_FILE = REPO_ROOT / "realworld_mapping.json"
EXTRACTION_PROFILE_REALWORLD_HUMAN = "realworld_human"
EXTRACTION_SYSTEM_PROMPT = "You are a precise JSON extractor. Return only valid JSON."
REALWORLD_HUMAN_EXTRACTION_PROMPT_TEMPLATE = """Analyze the model output below and extract one final textual answer exactly as reported.
The model output may be a single word, a short token, or a multiline program output.

Model output:
{model_output}

Rules:
1. Return exactly one valid JSON object with exactly these keys: {"rationale": <string>, "value": <string_or_null>}.
2. If no usable answer text is present, return {"rationale": "No valid textual answer found in the model output", "value": null}.
3. Preserve line order and internal newlines for multiline outputs.
4. Trim only leading/trailing whitespace around the whole extracted answer.
5. If the output contains multiple alternatives in one line (for example "A or B"), choose the first explicit answer candidate.
6. Do not invent content and do not infer missing lines.
7. Return only the JSON object and no additional text, markdown, or code fences.
"""

LENIENT_EXTRACTION_HINT = (
    "\n\nLenient extraction: If the output is clearly a shortened alias for a discrete label "
    '(for example one letter where the intended label is like "Replica A"), emit the full label when it '
    "is uniquely determined from that pattern. Otherwise copy the model output verbatim."
)

# Model-specific no-think prefix for Qwen
QWEN_NO_THINK_MODEL = "qwen/qwen3-32b"
QWEN_NO_THINK_PREFIX = "/no_think "

# Models that should receive an example-output suffix appended to the prompt
SUFFIX_MODELS = {
    "mistralai/Ministral-3-3B-Base-2512",
    "meta-llama/Llama-3.2-1B",
    "Qwen/Qwen3.5-2B-Base",
    "alpindale/Llama-3.2-1B",
}
SUFFIX_TEXT = "\n\nA valid example for this question is:"


def parse_extractor_json(result_text: str) -> Optional[Dict[str, Any]]:
    try:
        parsed = json.loads(strip_json_fence(result_text))
    except Exception:
        return None

    if not isinstance(parsed, dict) or not parsed.get("rationale"):
        return None

    value_candidate = parsed.get("value")
    if value_candidate is None:
        for alt_key in ("answer", "text", "output"):
            if alt_key in parsed:
                value_candidate = parsed.get(alt_key)
                break

    return {
        "rationale": parsed["rationale"],
        "value": realworld_mapping_helper.normalize_text_value(value_candidate),
    }


def strip_surrounding_code_fence(text: str) -> str:
    stripped = text.strip()
    if not (stripped.startswith("```") and stripped.endswith("```")):
        return stripped

    stripped = re.sub(r"^```[^\n]*\n?", "", stripped, count=1)
    stripped = re.sub(r"\n?```$", "", stripped)
    return stripped.strip()


def extract_realworld_with_regex(model_output: str) -> Dict[str, Any]:
    text = (model_output or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return {"rationale": "No textual output found via regex parsing", "value": None}

    text = strip_surrounding_code_fence(text)
    if "\n\n" in text:
        text = text.split("\n\n", 1)[0].rstrip()

    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and re.match(r"(?i)^(?:final\s+)?(?:answer|output|result)\s*:?\s*$", lines[0].strip()):
        lines = lines[1:]
    text = "\n".join(lines).strip()

    one_line_prefix = re.match(
        r"(?is)^(?:one\s+possible\s+output(?:\s+of\s+this\s+code)?|possible\s+output|output|answer|final\s+answer|final\s+output|result)\s*[:\-]\s*(.+)$",
        text,
    )
    if one_line_prefix and "\n" not in one_line_prefix.group(1):
        text = one_line_prefix.group(1).strip()

    if "\n" not in text:
        bullet_match = re.match(r"^\s*[-*]\s*(\S.+)$", text)
        if bullet_match:
            text = bullet_match.group(1).strip()

        explicit_match = re.match(r"(?is)^(?:the\s+)?(?:answer|output|result)\s+is\s+(.+)$", text)
        if explicit_match:
            text = explicit_match.group(1).strip()

    if "\n" not in text and " or " in text:
        text = text.split(" or ", 1)[0].strip()

    normalized = realworld_mapping_helper.normalize_text_value(text)
    if normalized is None:
        return {"rationale": "No textual output found via regex parsing", "value": None}

    return {
        "rationale": "Regex extracted textual output from model response",
        "value": normalized,
    }


def extract_value_with_provider(
    model_output: str,
    client: OpenAI,
    api_provider: str,
    extractor_model: str,
    extractor_api_provider: str,
    extractor_api_key: str,
    max_retries: int,
    retry_base_sleep: float,
    extraction_temperature: float,
    extraction_max_tokens: int,
    mapping_lenient: bool = False,
) -> Dict[str, Any]:
    if extractor_model.lower() == "regex":
        return extract_realworld_with_regex(model_output)

    extractor_client = client
    extractor_provider = extractor_api_provider
    if extractor_api_provider and extractor_api_provider != api_provider:
        extractor_client = build_client(extractor_api_provider, extractor_api_key)
    else:
        extractor_provider = api_provider

    user_content = REALWORLD_HUMAN_EXTRACTION_PROMPT_TEMPLATE.format(model_output=model_output)
    if mapping_lenient:
        user_content += LENIENT_EXTRACTION_HINT

    call_params = build_call_params(
        api_provider=extractor_provider,
        model=extractor_model,
        messages=[
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
        temperature=extraction_temperature,
        max_tokens=extraction_max_tokens,
    )

    try:
        response = create_chat_completion_with_retry(
            client=extractor_client,
            call_params=call_params,
            max_retries=max_retries,
            retry_base_sleep=retry_base_sleep,
            context_label=f"value extraction ({extractor_model}, profile={EXTRACTION_PROFILE_REALWORLD_HUMAN})",
        )
        parsed = parse_extractor_json((response.choices[0].message.content or "").strip())
        if parsed is None:
            return {"rationale": "None", "value": None}
        return parsed
    except Exception as exc:
        print(f"Error during extraction: {exc}")
        return {"rationale": "None", "value": None}


def extraction_result_has_value(extraction_result: Dict[str, Any]) -> bool:
    value = extraction_result.get("value")
    return isinstance(value, str) and bool(value.strip())


def build_followup_answer_only_prompt(original_prompt: str, failed_attempts: int, last_output: str) -> str:
    previous_output = (last_output or "").strip()
    return (
        original_prompt
        + f"\n\nIMPORTANT: I have already asked you {failed_attempts} times, and your previous output was:\n"
        + f"\"\"\"\n{previous_output}\n\"\"\"\n"
        + "That output did not contain a valid final answer for this question. "
        + "Do not explain, do not provide code, and do not add any extra text. "
        + "Return only the exact final textual output as instructed."
    )


def apply_model_prompt_prefix(model: str, prompt_text: str) -> str:
    if model == QWEN_NO_THINK_MODEL and not prompt_text.startswith(QWEN_NO_THINK_PREFIX):
        return QWEN_NO_THINK_PREFIX + prompt_text
    return prompt_text


def apply_model_prompt_suffix(model: str, prompt_text: str) -> str:
    if model in SUFFIX_MODELS:
        if not prompt_text.rstrip().endswith(SUFFIX_TEXT.strip()):
            return prompt_text + SUFFIX_TEXT
    return prompt_text


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Run realworld_human questions via OpenRouter/vLLM, extract an answer, and optionally "
            "retry until the extracted output exactly matches the expected format defined in "
            "realworld_mapping.json."
        )
    )

    p.add_argument(
        "--input_file",
        type=str,
        default=str(DEFAULT_QUESTIONS_FILE),
        help="Path to questions.json (default: realworld_human/questions.json)",
    )
    p.add_argument(
        "--mapping_file",
        type=str,
        default=str(DEFAULT_MAPPING_FILE),
        help="Path to realworld_mapping.json (default: UnpreditaBench/realworld_mapping.json)",
    )
    p.add_argument(
        "--output_dir",
        type=str,
        default="outputs_realworld_human",
        help="Directory to save the outputs (default: outputs_realworld_human)",
    )

    p.add_argument(
        "--api_provider",
        type=str,
        choices=["openrouter", "vllm"],
        default="openrouter",
        help="API provider to use",
    )
    p.add_argument(
        "--model",
        type=str,
        default="",
        help="Model ID (OpenRouter) or model name (vLLM)",
    )
    p.add_argument("--api_key", type=str, default="", help="API key")
    p.add_argument("--temp", type=float, default=0.7, help="Temperature for generation")
    p.add_argument("--max_tokens", type=int, default=4096, help="Max tokens to generate")
    p.add_argument(
        "--parallel_requests",
        type=int,
        default=64,
        help="Number of prompts to process concurrently",
    )

    p.add_argument("--max_retries", type=int, default=5, help="Max retry attempts for transient API errors")
    p.add_argument(
        "--retry_base_sleep",
        type=float,
        default=5.0,
        help="Base seconds for exponential backoff before jitter",
    )

    p.add_argument("--limit", type=int, default=None, help="Limit the number of prompts to process")
    p.add_argument("--verbose", action="store_true", help="Print responses to console")
    p.add_argument(
        "--resume",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Resume from existing per-uid output files in output_dir (default: enabled)",
    )

    p.add_argument(
        "--openrouter_provider",
        type=str,
        default="",
        help="Comma-separated OpenRouter provider order (e.g., 'OpenAI,Anthropic')",
    )

    p.add_argument(
        "--extract_value",
        dest="extract_value",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Enable/disable extraction from each model output (default: enabled)",
    )
    p.add_argument(
        "--extraction_retries",
        dest="extraction_retries",
        type=int,
        default=5,
        help="How many generation attempts to make if extracted output is unusable",
    )

    p.add_argument(
        "--value_extractor_model",
        dest="value_extractor_model",
        type=str,
        default="regex",
        help=(
            "Model used for extraction call (default: regex). "
            "Use 'regex' to run profile-specific parsing instead of an LLM."
        ),
    )
    p.add_argument(
        "--value_extractor_api_provider",
        dest="value_extractor_api_provider",
        type=str,
        choices=["", "openrouter", "vllm"],
        default="",
        help="API provider for value extractor (default: same as --api_provider)",
    )
    p.add_argument(
        "--value_extractor_api_key",
        dest="value_extractor_api_key",
        type=str,
        default="",
        help="API key for value extractor provider (default: same as --api_key)",
    )
    p.add_argument(
        "--value_extraction_temp",
        dest="value_extraction_temp",
        type=float,
        default=0.3,
        help="Temperature for extraction call",
    )
    p.add_argument(
        "--value_extraction_max_tokens",
        dest="value_extraction_max_tokens",
        type=int,
        default=128,
        help="Max tokens for extraction call",
    )

    p.add_argument(
        "--mapping_validate",
        action=argparse.BooleanOptionalAction,
        default=True,
        help=(
            "If enabled, and a mapping exists for the UID, generation is retried until the extracted "
            "value can be mapped/validated (default: enabled)."
        ),
    )
    p.add_argument(
        "--mapping_lenient",
        action=argparse.BooleanOptionalAction,
        default=False,
        help=(
            "Allow case-insensitive mapping matches and simple Replica <token> aliases "
            "when mapping validation is enabled (default: disabled)."
        ),
    )
    return p.parse_args()


def validate_args(args: argparse.Namespace) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    if not args.model:
        errors.append("--model is required")

    if args.api_provider == "openrouter" and not args.openrouter_provider:
        errors.append("--openrouter_provider is required when --api_provider openrouter is selected")

    if not args.api_key:
        errors.append("--api_key is required")

    if args.extraction_retries < 1:
        errors.append("--extraction_retries must be >= 1")

    if args.max_retries < 1:
        errors.append("--max_retries must be >= 1")

    if args.parallel_requests < 1:
        errors.append("--parallel_requests must be >= 1")

    input_path = Path(args.input_file)
    if not input_path.exists():
        errors.append(f"Input file not found: {input_path}")

    mapping_path = Path(args.mapping_file)
    if args.mapping_validate and not mapping_path.exists():
        errors.append(f"Mapping file not found: {mapping_path}")

    return (len(errors) == 0), errors


def get_unique_key(item: Dict[str, Any], idx: int) -> str:
    uid = item.get("uid")
    if uid:
        return str(uid)
    return f"{item.get('id', 'unknown')}_{idx}"


def get_result_path(output_dir: str, unique_key: str) -> str:
    safe_id = make_safe_id(unique_key)
    return os.path.join(output_dir, f"{safe_id}.json")


def save_individual_result(result_item: Dict[str, Any], output_dir: str, unique_key: str) -> str:
    output_file = get_result_path(output_dir, unique_key)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_item, f, indent=2)
    return output_file


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_mapping_multi(mapping_path: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Load mapping file into uid -> list[entry] (keeps duplicates)."""
    if not mapping_path.exists():
        return {}

    data = load_json(mapping_path)
    if not isinstance(data, dict):
        return {}

    index: Dict[str, List[Dict[str, Any]]] = {}

    for category, payload in data.items():
        if not isinstance(payload, dict):
            continue

        uids_key = "uids:" if "uids:" in payload else ("uids" if "uids" in payload else None)
        uids_list = payload.get(uids_key, []) if uids_key else []
        how_to_handle = payload.get("how_to_handle")

        if not isinstance(uids_list, list):
            continue

        for entry in uids_list:
            if not isinstance(entry, dict):
                continue

            uid = entry.get("value")
            metadata = entry.get("metadata", {}) or {}
            mapping_table = metadata.get("mapping") if isinstance(metadata, dict) else None

            if not uid:
                continue

            index.setdefault(str(uid), []).append(
                {
                    "category": category,
                    "how_to_handle": how_to_handle,
                    "metadata": metadata,
                    "mapping": mapping_table,
                }
            )

    return index


def _strip_trailing_punct_per_line(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        line = line.rstrip()
        # common LLM formatting artifacts
        line = line.rstrip("\t ")
        line = line.rstrip(".,;:!?")
        lines.append(line)
    return "\n".join(lines).strip()


def normalize_for_mapping(value: Any) -> Any:
    if value is None:
        return None

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value

    if not isinstance(value, str):
        return value

    normalized = realworld_mapping_helper.normalize_text_value(value)
    if normalized is None:
        return None

    normalized = _strip_trailing_punct_per_line(normalized)
    return normalized or None


def _find_lenient_mapping_key(value: str, mapping_table: Dict[str, Any]) -> Optional[str]:
    text = value.strip()
    if not text:
        return None

    text_cf = text.casefold()
    for key in mapping_table:
        if isinstance(key, str) and key.casefold() == text_cf:
            return key

    if " " not in text:
        for key in mapping_table:
            if not isinstance(key, str):
                continue
            key_cf = key.casefold()
            if key_cf.startswith("replica "):
                suffix = key_cf.split(" ", 1)[1]
                if suffix == text_cf:
                    return key

    return None


def lenient_canonicalize_to_mapping_key(
    uid: str,
    value: Any,
    mapping_multi: Dict[str, List[Dict[str, Any]]],
) -> Any:
    """Rewrite string answers to the exact mapping-table key when lenient aliases match."""
    if not isinstance(value, str):
        return value

    for entry in mapping_multi.get(uid, []):
        table = entry.get("mapping")
        if not isinstance(table, dict) or not table:
            continue
        if not any(isinstance(k, str) for k in table):
            continue
        canonical = _find_lenient_mapping_key(value, table)
        if canonical is not None:
            return canonical

    return value


def mapping_is_valid(entry: Dict[str, Any], label: Optional[Any], info: Optional[Any]) -> bool:
    how = entry.get("how_to_handle")
    if how == "shuffling":
        return isinstance(info, dict) and ("error" not in info) and (info.get("type") == "shuffling")
    return label is not None


def map_with_candidates(
    uid: str,
    extracted_value: Any,
    mapping_multi: Dict[str, List[Dict[str, Any]]],
    mapping_lenient: bool,
) -> Dict[str, Any]:
    candidates = mapping_multi.get(uid, [])
    if not candidates:
        return {
            "mapping_available": False,
            "mapping_valid": True,
            "mapping_category": None,
            "mapping_how_to_handle": None,
            "mapping_label": None,
            "mapped_value": None,
            "mapping_info": None,
        }

    mapping_input = normalize_for_mapping(extracted_value)

    first_info: Optional[Any] = None
    for entry in candidates:
        # Use the shared helper logic by passing a single-entry mapping index.
        label, info = realworld_mapping_helper.map_output_to_label(uid, mapping_input, {uid: entry})
        if first_info is None:
            first_info = info

        if not mapping_is_valid(entry, label, info):
            if not (
                mapping_lenient
                and isinstance(mapping_input, str)
                and isinstance(entry.get("mapping"), dict)
            ):
                continue

            alt_key = _find_lenient_mapping_key(mapping_input, entry["mapping"])
            if alt_key is None:
                continue
            try:
                label = int(entry["mapping"][alt_key])
            except Exception:
                continue
            info = alt_key

        mapped_value: Any = None
        if entry.get("how_to_handle") == "shuffling" and isinstance(info, dict):
            lines = info.get("lines")
            if isinstance(lines, list):
                mapped_value = "\n".join(str(x) for x in lines)
        elif label is not None:
            mapped_value = info

        return {
            "mapping_available": True,
            "mapping_valid": True,
            "mapping_category": entry.get("category"),
            "mapping_how_to_handle": entry.get("how_to_handle"),
            "mapping_label": label,
            "mapped_value": mapped_value,
            "mapping_info": info,
        }

    # No candidate matched.
    return {
        "mapping_available": True,
        "mapping_valid": False,
        "mapping_category": candidates[0].get("category") if candidates else None,
        "mapping_how_to_handle": candidates[0].get("how_to_handle") if candidates else None,
        "mapping_label": None,
        "mapped_value": None,
        "mapping_info": first_info,
    }


RESUME_REQUIRED_FIELDS = (
    "uid",
    "model_output",
    "finish_reason",
    "generation_attempts_used",
    "reinforced_prompt_used",
)


def load_existing_result_for_item(
    item: Dict[str, Any],
    output_dir: str,
    unique_key: str,
    args: argparse.Namespace,
) -> Optional[Dict[str, Any]]:
    output_file = get_result_path(output_dir, unique_key)
    if not os.path.exists(output_file):
        return None

    try:
        with open(output_file, "r", encoding="utf-8") as f:
            existing = json.load(f)
    except Exception as exc:
        print(f"Warning: could not parse existing result for uid {unique_key} ({output_file}): {exc}")
        return None

    if not isinstance(existing, dict):
        return None

    for field in RESUME_REQUIRED_FIELDS:
        if field not in existing:
            return None

    # If extraction is expected, make sure extracted fields exist.
    if args.extract_value and "extracted_value" not in existing:
        return None

    # If mapping validation is enabled and mapping fields are missing, re-run.
    if args.mapping_validate and "mapping_valid" not in existing:
        return None

    if args.mapping_validate and existing.get("mapping_lenient_enabled") != bool(args.mapping_lenient):
        return None

    return existing


def process_prompt_item(
    item: Dict[str, Any],
    idx: int,
    args: argparse.Namespace,
    provider_order: List[str],
    mapping_multi: Dict[str, List[Dict[str, Any]]],
) -> Optional[Dict[str, Any]]:
    prompt_text = item.get("prompt_text")
    uid = str(item.get("uid", "")).strip()

    if not prompt_text:
        print(f"Skipping item at idx={idx}: missing 'prompt_text'.")
        return None

    if not uid:
        print(f"Skipping item at idx={idx}: missing 'uid'.")
        return None

    extractor_model = (args.value_extractor_model or "").strip() or args.model
    extractor_api_provider = (args.value_extractor_api_provider or "").strip() or args.api_provider
    extractor_api_key = (args.value_extractor_api_key or "").strip() or args.api_key

    extraction_profile = EXTRACTION_PROFILE_REALWORLD_HUMAN
    generation_attempts = args.extraction_retries if args.extract_value else 1

    selected_output_text: Optional[str] = None
    selected_finish_reason: Optional[str] = None
    extraction_result: Dict[str, Any] = {"rationale": "None", "value": None}
    mapping_result: Dict[str, Any] = {
        "mapping_available": False,
        "mapping_valid": True,
        "mapping_category": None,
        "mapping_how_to_handle": None,
        "mapping_label": None,
        "mapped_value": None,
        "mapping_info": None,
    }

    used_generation_attempts = 0
    reinforced_prompt_used = False

    client = build_client(args.api_provider, args.api_key)

    followup_attempts = 1 if args.extract_value else 0
    total_generation_attempts = generation_attempts + followup_attempts

    for gen_attempt in range(1, total_generation_attempts + 1):
        used_generation_attempts = gen_attempt

        current_prompt_text = apply_model_prompt_prefix(args.model, prompt_text)
        current_prompt_text = apply_model_prompt_suffix(args.model, current_prompt_text)
        is_followup_attempt = gen_attempt > generation_attempts
        if is_followup_attempt:
            reinforced_prompt_used = True
            current_prompt_text = build_followup_answer_only_prompt(
                original_prompt=current_prompt_text,
                failed_attempts=generation_attempts,
                last_output=selected_output_text or "",
            )

        generation_call_params = build_call_params(
            api_provider=args.api_provider,
            model=args.model,
            messages=[{"role": "user", "content": current_prompt_text}],
            temperature=args.temp,
            max_tokens=args.max_tokens,
            provider_order=provider_order,
        )

        response = create_chat_completion_with_retry(
            client=client,
            call_params=generation_call_params,
            max_retries=args.max_retries,
            retry_base_sleep=args.retry_base_sleep,
            context_label=f"generation for uid={uid}",
        )

        model_output = response.choices[0].message.content
        finish_reason = getattr(response.choices[0], "finish_reason", None)

        if args.verbose:
            print(f"\n--- UID: {uid} (attempt {gen_attempt}/{generation_attempts}) ---\n{model_output}\n")

        selected_output_text = model_output
        selected_finish_reason = finish_reason

        if not args.extract_value:
            break

        extraction_result = extract_value_with_provider(
            model_output=model_output,
            client=client,
            api_provider=args.api_provider,
            extractor_model=extractor_model,
            extractor_api_provider=extractor_api_provider,
            extractor_api_key=extractor_api_key,
            max_retries=args.max_retries,
            retry_base_sleep=args.retry_base_sleep,
            extraction_temperature=args.value_extraction_temp,
            extraction_max_tokens=args.value_extraction_max_tokens,
            mapping_lenient=args.mapping_lenient,
        )

        if not extraction_result_has_value(extraction_result):
            if gen_attempt < generation_attempts:
                print(
                    f"No extractable text for uid={uid} on attempt {gen_attempt}/{generation_attempts}; retrying generation."
                )
            elif gen_attempt == generation_attempts and followup_attempts > 0:
                print(
                    f"No extractable text for uid={uid} after {generation_attempts} attempts; retrying once with reinforced answer-only instructions."
                )
            continue

        extracted_value = normalize_for_mapping(extraction_result.get("value"))
        if args.mapping_lenient:
            extracted_value = lenient_canonicalize_to_mapping_key(uid, extracted_value, mapping_multi)
        extraction_result["value"] = extracted_value
        mapping_result = map_with_candidates(uid, extracted_value, mapping_multi, args.mapping_lenient)

        if args.mapping_validate and mapping_result.get("mapping_available") and not mapping_result.get("mapping_valid"):
            if gen_attempt < generation_attempts:
                print(
                    f"Extracted value did not match mapping for uid={uid} on attempt {gen_attempt}/{generation_attempts}; retrying generation."
                )
            elif gen_attempt == generation_attempts and followup_attempts > 0:
                print(
                    f"Extracted value did not match mapping for uid={uid} after {generation_attempts} attempts; retrying once with reinforced answer-only instructions."
                )
            continue

        # Success: extracted a value; and (if mapping exists) it validated.
        break

    result_item = item.copy()

    result_item["model_output"] = selected_output_text
    result_item["model_used"] = args.model
    result_item["api_provider"] = args.api_provider
    result_item["temperature"] = args.temp
    result_item["max_tokens"] = args.max_tokens
    result_item["finish_reason"] = selected_finish_reason
    result_item["generation_attempts_used"] = used_generation_attempts
    result_item["reinforced_prompt_used"] = reinforced_prompt_used

    result_item["extract_value_enabled"] = bool(args.extract_value)
    result_item["extraction_profile"] = extraction_profile if args.extract_value else None
    result_item["value_extractor_model"] = extractor_model if args.extract_value else None
    result_item["rationale"] = extraction_result.get("rationale") if args.extract_value else None
    result_item["extracted_value"] = extraction_result.get("value") if args.extract_value else None

    result_item.update(mapping_result)
    result_item["mapping_lenient_enabled"] = bool(args.mapping_lenient)

    if args.api_provider == "openrouter":
        result_item["openrouter_provider_order"] = provider_order if provider_order else None
        result_item["openrouter_allow_fallbacks"] = False if provider_order else None
    else:
        result_item["openrouter_provider_order"] = None

    return result_item


def main() -> None:
    args = parse_args()
    is_valid, validation_errors = validate_args(args)
    if not is_valid:
        for err in validation_errors:
            print(f"Error: {err}")
        raise SystemExit(2)

    provider_order = parse_provider_order(args.api_provider, args.openrouter_provider)
    data = load_input_data(args.input_file, args.limit)
    output_dir = ensure_output_dir(args.output_dir)

    mapping_path = Path(args.mapping_file).resolve()
    mapping_multi = load_mapping_multi(mapping_path)

    duplicate_uids = realworld_mapping_helper.find_duplicate_uids(mapping_path) if mapping_path.exists() else []
    if duplicate_uids:
        print(f"Warning: duplicate UIDs found in mapping file: {duplicate_uids}")

    q_uids = [str(item.get("uid", "")).strip() for item in data if isinstance(item, dict)]
    missing_in_mapping = sorted({u for u in q_uids if u and u not in mapping_multi})
    if args.mapping_validate and missing_in_mapping:
        print(
            "Warning: mapping_validate is enabled but these uids are missing from mapping; "
            "they will be treated as 'no mapping' (no mapping-based retry):\n - "
            + "\n - ".join(missing_in_mapping)
        )

    print(
        f"Processing {len(data)} prompts using {args.api_provider} with model {args.model} "
        f"(temp={args.temp}, extract_value={args.extract_value}, mapping_validate={args.mapping_validate}, "
        f"mapping_lenient={args.mapping_lenient}, parallel_requests={args.parallel_requests}, resume={args.resume})..."
    )

    indexed_results: Dict[int, Dict[str, Any]] = {}
    pending_items: List[Tuple[int, Dict[str, Any], str]] = []

    if args.resume:
        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                continue
            unique_key = get_unique_key(item, idx)
            existing = load_existing_result_for_item(item, output_dir, unique_key, args)
            if existing is not None:
                indexed_results[idx] = existing
            else:
                pending_items.append((idx, item, unique_key))
        print(
            f"Resume enabled: found {len(indexed_results)} existing results, {len(pending_items)} prompts pending."
        )
    else:
        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                continue
            pending_items.append((idx, item, get_unique_key(item, idx)))
        print(f"Resume disabled: processing all {len(pending_items)} prompts.")

    def _run_one(idx: int, item: Dict[str, Any], unique_key: str) -> Optional[Dict[str, Any]]:
        return process_prompt_item(
            item=item,
            idx=idx,
            args=args,
            provider_order=provider_order,
            mapping_multi=mapping_multi,
        )

    if args.parallel_requests == 1:
        for idx, item, unique_key in tqdm(pending_items):
            try:
                result_item = _run_one(idx, item, unique_key)
                if result_item is None:
                    continue
                indexed_results[idx] = result_item
                save_individual_result(result_item, output_dir, unique_key)
            except Exception as exc:
                print(f"Error processing uid={unique_key}: {exc}")
    else:
        with ThreadPoolExecutor(max_workers=args.parallel_requests) as executor:
            future_to_key = {
                executor.submit(_run_one, idx, item, unique_key): (idx, unique_key)
                for (idx, item, unique_key) in pending_items
            }

            for future in tqdm(as_completed(future_to_key), total=len(future_to_key)):
                idx, unique_key = future_to_key[future]
                try:
                    result_item = future.result()
                    if result_item is None:
                        continue
                    indexed_results[idx] = result_item
                    save_individual_result(result_item, output_dir, unique_key)
                except Exception as exc:
                    print(f"Error processing uid={unique_key}: {exc}")

    results: List[Dict[str, Any]] = [indexed_results[i] for i in sorted(indexed_results)]
    final_output = save_summary(results, output_dir)

    print(f"\nDone! Processed {len(results)} prompts.")
    print(f"Results saved to: {output_dir}")
    print(f"Summary file: {final_output}")


if __name__ == "__main__":
    main()
