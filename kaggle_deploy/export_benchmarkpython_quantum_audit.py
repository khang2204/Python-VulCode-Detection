#!/usr/bin/env python3
"""Retain a small, reproducible TP/TN audit set from one Quantum run."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def select(rows: list[dict], true_label: int, predicted_label: int, count: int) -> list[dict]:
    matches = [
        row for row in rows
        if int(row["true_label"]) == true_label and int(row["predicted_label"]) == predicted_label
    ]
    return sorted(matches, key=lambda row: str(row["sample_file"]))[:count]


def copy_source(row: dict, destination: Path) -> None:
    source = Path(str(row["sample_file"]))
    if source.is_file():
        shutil.copy2(source, destination / source.name)
        row["retained_source_file"] = source.name
    else:
        row["retained_source_file"] = None
        row["source_copy_status"] = "sample_file is not available on this local machine"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--count", type=int, default=2)
    args = parser.parse_args()

    rows = json.loads(args.predictions.read_text(encoding="utf-8"))
    selected = {
        "true_positive": select(rows, true_label=1, predicted_label=1, count=args.count),
        "true_negative": select(rows, true_label=0, predicted_label=0, count=args.count),
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for label, examples in selected.items():
        source_dir = args.out_dir / label
        source_dir.mkdir(exist_ok=True)
        for row in examples:
            copy_source(row, source_dir)
    (args.out_dir / "audit_predictions.json").write_text(
        json.dumps(selected, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({label: len(examples) for label, examples in selected.items()}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
