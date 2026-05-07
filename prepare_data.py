import json
from pathlib import Path
from datasets import load_dataset

dataset_name = "UnpredictaBench/UnpredictaBench"
out_dir = Path("data")
out_dir.mkdir(exist_ok=True)

ds = load_dataset(dataset_name)

rows = ds["train"]

tasks = {}

for row in rows:
    row = dict(row)

    task_name = row.pop("task", None)

    if task_name is None:
        task_name = row.get("category", "unknown")

    tasks.setdefault(task_name, []).append(row)

for task_name, task_rows in tasks.items():
    task_dir = out_dir / task_name
    task_dir.mkdir(parents=True, exist_ok=True)

    with open(task_dir / "questions.json", "w", encoding="utf-8") as f:
        json.dump(task_rows, f, ensure_ascii=False, indent=2)

print(f"Saved {sum(len(v) for v in tasks.values())} examples into {len(tasks)} task folders.")