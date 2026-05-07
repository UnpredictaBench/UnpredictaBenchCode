#!/usr/bin/env python3

import argparse
import json
import uuid
from pathlib import Path
from typing import Dict, List, Tuple


def load_json_array(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array in {path}")
    return data


def deterministic_id(root: Path, questions_path: Path, index: int) -> str:
    rel_path = questions_path.relative_to(root).as_posix()
    token = f"{rel_path}:{index}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, token))


def update_questions_ids(root: Path, questions_path: Path) -> Tuple[List[dict], Dict[str, str]]:
    questions = load_json_array(questions_path)

    old_id_to_uid: Dict[str, str] = {}

    for i, item in enumerate(questions):
        if not isinstance(item, dict):
            raise ValueError(f"Expected object entries in {questions_path}, found {type(item).__name__}")
        new_uid = deterministic_id(root, questions_path, i)
        old_id = item.get("id")
        item["uid"] = new_uid
        if isinstance(old_id, str) and old_id:
            old_id_to_uid.setdefault(old_id, new_uid)

    return questions, old_id_to_uid


def update_all_results_ids(
    results: List[dict],
    old_id_to_uid: Dict[str, str],
) -> Tuple[int, int]:
    updated = 0
    unmatched = 0

    for item in results:
        if not isinstance(item, dict):
            continue

        old_id = item.get("id")
        if isinstance(old_id, str) and old_id in old_id_to_uid:
            item["uid"] = old_id_to_uid[old_id]
            updated += 1
        else:
            unmatched += 1

    return updated, unmatched


def write_json_array(path: Path, data: List[dict], dry_run: bool) -> None:
    if dry_run:
        return
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def process_folder(root: Path, dry_run: bool, verbose: bool) -> None:
    question_files = sorted(root.rglob("questions.json"))

    if not question_files:
        print(f"No questions.json files found under: {root}")
        return

    total_questions_files = 0
    total_question_rows = 0
    total_results_files = 0
    total_results_rows_updated = 0
    total_results_rows_unmatched = 0

    for q_path in question_files:
        total_questions_files += 1
        questions, old_id_to_uid = update_questions_ids(root, q_path)
        write_json_array(q_path, questions, dry_run)
        total_question_rows += len(questions)

        r_path = q_path.parent / "all_results.json"
        if r_path.exists():
            results = load_json_array(r_path)
            updated, unmatched = update_all_results_ids(results, old_id_to_uid)
            write_json_array(r_path, results, dry_run)

            total_results_files += 1
            total_results_rows_updated += updated
            total_results_rows_unmatched += unmatched

            if verbose:
                print(
                    f"[all_results] {r_path} -> updated={updated}, unmatched={unmatched}, total={len(results)}"
                )

        if verbose:
            print(f"[questions] {q_path} -> updated={len(questions)}")

    print("Completed ID replacement")
    print(f"Root: {root}")
    print(f"questions.json files processed: {total_questions_files}")
    print(f"question rows updated: {total_question_rows}")
    print(f"all_results.json files processed: {total_results_files}")
    print(f"all_results rows updated: {total_results_rows_updated}")
    print(f"all_results rows unmatched: {total_results_rows_unmatched}")
    print(f"Mode: {'dry-run' if dry_run else 'write'}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Recursively add uid values in questions.json and mirror those uids "
            "to sibling all_results.json files by matching existing id values."
        )
    )
    parser.add_argument(
        "root",
        type=Path,
        help="Root folder to scan recursively",
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

    process_folder(root=root, dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    main()
