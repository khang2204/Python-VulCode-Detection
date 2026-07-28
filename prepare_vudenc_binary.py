#!/usr/bin/env python3
"""Prepare every labelled VUDENC block for Joern-based CPG construction.

No Python ``ast.parse`` pre-filter is used: VUDENC contains statement-context
blocks that are not necessarily valid standalone Python modules. Joern is the
sole parser/graph-construction gate; only its graph-export results decide the
final usable corpus.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path


def primary_type(labels: list[int]) -> int:
    positive = [label for label in labels if label > 0]
    return Counter(positive).most_common(1)[0][0]


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=root / "data" / "Vudenc")
    parser.add_argument("--out-dir", type=Path, default=root / "CPG" / "Vudenc")
    args = parser.parse_args()
    try:
        import pyarrow.parquet as pq
    except ImportError as error:
        raise SystemExit("pyarrow is required to read VUDENC parquet files.") from error

    paths = [args.input_dir / name for name in ("train.parquet", "test.parquet")]
    if any(not path.is_file() for path in paths):
        raise SystemExit("Missing VUDENC train.parquet/test.parquet input files.")

    records = []
    excluded = Counter()
    for split, path in zip(("train", "test"), paths):
        for index, item in enumerate(pq.read_table(path).to_pylist()):
            raw_lines, labels = item["raw_lines"], item["label"]
            if len(raw_lines) != len(labels):
                excluded["label_length_mismatch"] += 1
                continue
            source = "".join(raw_lines)
            label = int(any(value > 0 for value in labels))
            category = f"VUDENC-TYPE-{primary_type(labels)}" if label else "BENIGN"
            digest = hashlib.sha256((split + "\0" + str(index) + "\0" + source).encode()).hexdigest()[:20]
            records.append(
                {
                    "sample_id": f"vudenc_{digest}",
                    "source": source,
                    "label": label,
                    "category": category,
                    "split": split,
                    "source_index": index,
                    "line_labels": labels,
                }
            )

    out_dir = args.out_dir.resolve()
    source_root = out_dir / "source" / "vudenc"
    if source_root.exists():
        shutil.rmtree(source_root)
    source_root.mkdir(parents=True, exist_ok=True)
    metadata = []
    for record in records:
        filename = f"{record['sample_id']}.py"
        (source_root / filename).write_text(record["source"], encoding="utf-8")
        metadata.append(
            {
                "sample_file": f"vudenc/{filename}",
                "pair_id": record["sample_id"],
                "version": "single",
                "real_vulnerability": "true" if record["label"] else "false",
                "cwe": record["category"],
                "source_cwe": record["category"],
                "source_split": record["split"],
                "source_index": record["source_index"],
                "line_labels": record["line_labels"],
                "source_sha256": hashlib.sha256(record["source"].encode()).hexdigest(),
            }
        )
    metadata_path = out_dir / "metadata.jsonl"
    metadata_path.write_text("".join(json.dumps(record, sort_keys=True) + "\n" for record in metadata), encoding="utf-8")
    report = {
        "dataset": "VUDENC",
        "representation": "raw_statement_context_blocks",
        "raw_labelled_samples": len(metadata),
        "binary_counts": {
            "benign": sum(record["real_vulnerability"] == "false" for record in metadata),
            "vulnerable": sum(record["real_vulnerability"] == "true" for record in metadata),
        },
        "vulnerable_type_counts": dict(sorted(Counter(record["cwe"] for record in metadata if record["real_vulnerability"] == "true").items())),
        "excluded_before_joern": dict(excluded),
        "metadata": str(metadata_path),
        "source_root": str(source_root),
    }
    (out_dir / "prepare_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
