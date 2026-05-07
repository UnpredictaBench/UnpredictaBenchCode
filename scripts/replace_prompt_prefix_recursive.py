#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import List, Tuple


def load_json_array(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {path}")
    return data


def write_json_array(path: Path, data: List[dict], dry_run: bool) -> None:
    if dry_run:
        return
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def merge_prefix_and_body(new_prefix: str, body: str) -> str:
    if new_prefix.endswith("\n") and body.startswith("\n"):
        return new_prefix + body[1:]
    if (not new_prefix.endswith("\n")) and (not body.startswith("\n")):
        return new_prefix + "\n" + body
    return new_prefix + body


def replace_prompt_prefix(
    prompt: str,
    new_prefix: str,
    old_prefix: str,
) -> Tuple[str, bool]:
    if not prompt.startswith(old_prefix):
        return prompt, False

    body = prompt[len(old_prefix) :]
    return merge_prefix_and_body(new_prefix, body), True


def process_questions_file(
    questions_path: Path,
    new_prefix: str,
    old_prefix: str,
    dry_run: bool,
) -> Tuple[int, int, int]:
    questions = load_json_array(questions_path)

    updated = 0
    scanned = 0
    skipped = 0

    for item in questions:
        if not isinstance(item, dict):
            continue

        prompt = item.get("prompt_text")
        if not isinstance(prompt, str):
            continue

        scanned += 1
        new_prompt, changed = replace_prompt_prefix(
            prompt=prompt,
            new_prefix=new_prefix,
            old_prefix=old_prefix,
        )
        if changed and new_prompt != prompt:
            item["prompt_text"] = new_prompt
            updated += 1
        elif not changed:
            skipped += 1

    write_json_array(questions_path, questions, dry_run)
    return scanned, updated, skipped


def process_folder(
    root: Path,
    new_prefix: str,
    old_prefix: str,
    dry_run: bool,
    verbose: bool,
) -> None:
    question_files = sorted(root.rglob("questions.json"))

    if not question_files:
        print(f"No questions.json files found under: {root}")
        return

    total_files = 0
    total_scanned = 0
    total_updated = 0
    total_skipped = 0

    for q_path in question_files:
        scanned, updated, skipped = process_questions_file(
            questions_path=q_path,
            new_prefix=new_prefix,
            old_prefix=old_prefix,
            dry_run=dry_run,
        )
        total_files += 1
        total_scanned += scanned
        total_updated += updated
        total_skipped += skipped

        if skipped > 0:
            print(f"SKIP {q_path}: old prefix not found in {skipped} prompt_text field(s)")

        if verbose:
            print(f"{q_path}: updated={updated}, skipped={skipped}, scanned={scanned}")

    print("Completed prompt_text prefix replacement")
    print(f"Root: {root}")
    print(f"questions.json files processed: {total_files}")
    print(f"prompt_text fields scanned: {total_scanned}")
    print(f"prompt_text fields updated: {total_updated}")
    print(f"prompt_text fields skipped: {total_skipped}")
    print(f"Mode: {'dry-run' if dry_run else 'write'}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively find questions.json files and replace prompt_text prefix by exact match."
        )
    )
    parser.add_argument(
        "root",
        type=Path,
        help="Root folder to scan recursively",
    )
    parser.add_argument(
        "--new-prefix",
        required=True,
        help="New prefix text to place before the code block in prompt_text",
    )
    parser.add_argument(
        "--old-prefix",
        required=True,
        help="Exact old prefix to replace (must match at start of prompt_text)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute and report changes without writing files",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-file details",
    )

    args = parser.parse_args()
    root = args.root.resolve()

    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Root path is not a directory: {root}")

    process_folder(
        root=root,
        new_prefix=args.new_prefix,
        old_prefix=args.old_prefix,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()