"""Utilities for reading and applying `realworld_mapping.json`.

Provides:
- `load_mapping(path)` -> uid-indexed dict
- `map_output_to_label(uid, output, mapping_index)` -> (label, matched_key_or_info)
- `find_duplicate_uids(path)` -> list of duplicate uids

This helper is conservative: it performs exact-match mapping for entries
that provide a `mapping` table. For `shuffling` entries it returns a
normalized list of lines (caller can decide how to convert to an index).
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def load_mapping(path: Path) -> Dict[str, Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    index: Dict[str, Dict[str, Any]] = {}

    for category, payload in data.items():
        # tolerate both 'uids' and 'uids:' keys (file uses 'uids:')
        uids_key = "uids:" if "uids:" in payload else ("uids" if "uids" in payload else None)
        uids_list = payload.get(uids_key, []) if uids_key else []
        how_to_handle = payload.get("how_to_handle")

        for entry in uids_list:
            uid = entry.get("value")
            metadata = entry.get("metadata", {}) or {}
            mapping_table = metadata.get("mapping") if isinstance(metadata, dict) else None

            index[uid] = {
                "category": category,
                "how_to_handle": how_to_handle,
                "metadata": metadata,
                "mapping": mapping_table,
            }

    return index


def _strip_code_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```") and t.endswith("```"):
        t = re.sub(r"^```[^\n]*\n?", "", t, count=1)
        t = re.sub(r"\n?```$", "", t)
    return t


def normalize_text_value(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        text = str(value)
    elif isinstance(value, str):
        text = value
    else:
        return None

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _strip_code_fence(text)
    # trim trailing spaces on each line, preserve internal newlines
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = text.strip()
    if not text:
        return None
    # unwrap matching surrounding quotes
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ("'", '"'):
        text = text[1:-1].strip()
    return text or None


def map_output_to_label(
    uid: str, output: Any, mapping_index: Dict[str, Dict[str, Any]]
) -> Tuple[Optional[int], Optional[Any]]:
    """Map a model output to an integer label using the mapping index.

    Returns (label, matched_key_or_info). If no integer label is defined
    for the UID/observed output, returns (None, info) where info may be
    a normalized string, a list of lines (for shuffling), or None.
    """
    entry = mapping_index.get(uid)
    if entry is None:
        return None, None

    how = entry.get("how_to_handle")
    metadata = entry.get("metadata", {}) or {}
    mapping_table = entry.get("mapping") or metadata.get("mapping")

    if how == "mapping_as_distribution" or mapping_table:
        normalized = normalize_text_value(output)
        # explicit (no output) token handling
        if normalized is None and mapping_table and "(no output)" in mapping_table:
            return int(mapping_table["(no output)"]), "(no output)"

        if normalized is None:
            return None, None

        if mapping_table is None:
            if metadata.get("type") == "number":
                try:
                    if "." in normalized or "e" in normalized.lower():
                        val = float(normalized)
                    else:
                        val = int(normalized)
                    return val, val
                except Exception:
                    return None, normalized
            return None, normalized

        if normalized in mapping_table:
            return int(mapping_table[normalized]), normalized

        # fallback: try collapsing inner whitespace on each line
        collapsed = "\n".join(" ".join(line.split()) for line in normalized.split("\n"))
        if collapsed in mapping_table:
            return int(mapping_table[collapsed]), collapsed

        return None, normalized

    if how == "shuffling":
        normalized = normalize_text_value(output)
        if normalized is None:
            return None, None
        lines = [line for line in normalized.split("\n") if line != ""]
        expected = metadata.get("number_of_lines")
        if expected is not None and len(lines) != expected:
            return None, {"error": f"expected {expected} lines, got {len(lines)}", "lines": lines}
        return None, {"type": "shuffling", "lines": lines}

    if how == "single_item_selection":
        t = metadata.get("type")
        mapping_table = metadata.get("mapping")
        if t == "number":
            # try to parse as number
            normalized = normalize_text_value(output)
            if normalized is None:
                return None, None
            try:
                if "." in normalized or "e" in normalized.lower():
                    val = float(normalized)
                else:
                    val = int(normalized)
                return val, val
            except Exception:
                return None, normalized

        # default: string mapping
        normalized = normalize_text_value(output)
        if normalized is None:
            return None, None
        if mapping_table and normalized in mapping_table:
            return int(mapping_table[normalized]), normalized
        return None, normalized

    # unknown handling
    return None, None


def find_duplicate_uids(path: Path) -> List[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    seen: Dict[str, int] = {}
    duplicates: List[str] = []
    for category, payload in data.items():
        uids_key = "uids:" if "uids:" in payload else ("uids" if "uids" in payload else None)
        uids_list = payload.get(uids_key, []) if uids_key else []
        for entry in uids_list:
            uid = entry.get("value")
            seen[uid] = seen.get(uid, 0) + 1
            if seen[uid] == 2:
                duplicates.append(uid)
    return duplicates


def _main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("mapping_file", type=Path, help="Path to realworld_mapping.json")
    p.add_argument("--report-duplicates", action="store_true")
    args = p.parse_args(argv)

    mapping_index = load_mapping(args.mapping_file)
    print(f"Loaded {len(mapping_index)} UIDs from {args.mapping_file}")

    if args.report_duplicates:
        dups = find_duplicate_uids(args.mapping_file)
        if not dups:
            print("No duplicate UIDs found")
        else:
            print("Duplicate UIDs:")
            for u in dups:
                print(" -", u)

    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
