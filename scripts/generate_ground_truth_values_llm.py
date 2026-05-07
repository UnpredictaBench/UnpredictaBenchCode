import argparse
import ast
import json
import logging
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

from tqdm import tqdm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run generated Python files in ground_truth_codes and save per-UID "
            "ground truth lists under mirrored directories in ground_truth_values."
        )
    )
    parser.add_argument(
        "--codes-root",
        type=Path,
        default=Path("ground_truth_codes"),
        help="Root directory containing generated Python files.",
    )
    parser.add_argument(
        "--values-root",
        type=Path,
        default=Path("ground_truth_values"),
        help="Output root directory for JSON value files.",
    )
    parser.add_argument(
        "--output-filename",
        type=str,
        default="ground_truth_values.json",
        help="JSON filename to write inside each mirrored output directory.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=120,
        help="Timeout for each executed Python file.",
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


def list_code_directories(codes_root: Path) -> List[Path]:
    if not codes_root.exists() or not codes_root.is_dir():
        raise FileNotFoundError(f"Codes root not found or not a directory: {codes_root}")
    excluded = {"realworld_human", "shuffling_human"}
    return sorted([p for p in codes_root.iterdir() if p.is_dir() and p.name not in excluded])


def run_python_file(py_file: Path, timeout_seconds: int) -> Tuple[bool, str, str]:
    try:
        proc = subprocess.run(
            [sys.executable, str(py_file)],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        return False, "", f"Execution timed out after {timeout_seconds}s"

    if proc.returncode != 0:
        return (
            False,
            proc.stdout,
            f"Execution failed (code={proc.returncode})\nSTDERR:\n{proc.stderr.strip()}",
        )

    return True, proc.stdout, ""


def extract_last_list_text(stdout_text: str) -> Optional[str]:
    # Match all bracketed expressions and use the last one, which should be the printed list.
    matches = list(re.finditer(r"\[[\s\S]*?\]", stdout_text))
    if not matches:
        return None
    return matches[-1].group(0)


def strip_numpy_scalar_wrappers(text: str) -> str:
    # Examples handled: np.int64(3), np.float32(1.2), numpy.float64(5.6)
    pattern = re.compile(r"\b(?:np|numpy)\.[A-Za-z_][A-Za-z0-9_]*\(([^()]+)\)")
    out = text
    for _ in range(20):
        new_out = pattern.sub(r"\1", out)
        if new_out == out:
            break
        out = new_out
    return out


def parse_ground_truth_values(stdout_text: str) -> Tuple[Optional[List[float]], str]:
    list_text = extract_last_list_text(stdout_text)
    if not list_text:
        return None, "Could not find a printed list in stdout."

    normalized = strip_numpy_scalar_wrappers(list_text)

    try:
        parsed = ast.literal_eval(normalized)
    except Exception as exc:  # noqa: BLE001
        return None, f"Failed to parse printed list: {exc}"

    if not isinstance(parsed, list):
        return None, "Parsed object is not a list."

    if len(parsed) != 10000:
        return None, f"List length is {len(parsed)}, expected 10000."

    output: List[float] = []
    for item in parsed:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return None, "List contains non-numeric value(s)."
        output.append(float(item) if isinstance(item, float) else int(item))

    return output, ""


def write_directory_output(output_file: Path, records: List[dict[str, Any]]) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)


def main() -> None:
    args = parse_args()
    configure_logging(args.log_level)

    code_dirs = list_code_directories(args.codes_root)
    args.values_root.mkdir(parents=True, exist_ok=True)

    total_files = 0
    ok_files = 0
    failed_files = 0

    logging.info("Found %d code directories under %s", len(code_dirs), args.codes_root)

    for code_dir in tqdm(code_dirs, desc="Directories", unit="dir"):
        py_files = sorted(code_dir.glob("*.py"))
        output_records: List[dict[str, Any]] = []

        tqdm.write(f"Processing {code_dir.name}: {len(py_files)} python files")

        for py_file in tqdm(py_files, desc=code_dir.name, unit="file", leave=False):
            total_files += 1
            uid = py_file.stem

            ran_ok, stdout_text, run_error = run_python_file(py_file, args.timeout_seconds)
            if not ran_ok:
                failed_files += 1
                logging.warning("%s failed to execute: %s", py_file, run_error)
                continue

            values, parse_error = parse_ground_truth_values(stdout_text)
            if values is None:
                failed_files += 1
                logging.warning("%s output parsing failed: %s", py_file, parse_error)
                continue

            output_records.append(
                {
                    "uid": uid,
                    "ground_truth_values": values,
                }
            )
            ok_files += 1

        mirrored_output_dir = args.values_root / code_dir.name
        output_file = mirrored_output_dir / args.output_filename
        write_directory_output(output_file, output_records)
        tqdm.write(f"Saved {len(output_records)} records -> {output_file}")

    tqdm.write("\nDone.")
    tqdm.write(f"Total files processed: {total_files}")
    tqdm.write(f"Successful files:      {ok_files}")
    tqdm.write(f"Failed files:          {failed_files}")


if __name__ == "__main__":
    main()
