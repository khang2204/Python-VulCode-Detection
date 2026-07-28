#!/usr/bin/env python3
"""Identify test records that Quantum flags but Classical correctly keeps benign."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> dict[str, dict]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    return {row["sample_file"]: row for row in rows}


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quantum", type=Path, default=root / "visualize_result/vudenc_quantum_false_positives/test_predictions.json")
    parser.add_argument("--classical", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=root / "visualize_result/vudenc_quantum_only_false_positives.json")
    parser.add_argument("--source-root", type=Path, default=root / "CPG/Vudenc/source")
    parser.add_argument("--source-out", type=Path, default=root / "visualize_result/vudenc_quantum_only_false_positive_sources")
    args = parser.parse_args()
    quantum, classical = load(args.quantum), load(args.classical)
    if quantum.keys() != classical.keys():
        raise RuntimeError("Quantum and Classical prediction files do not cover the same test samples.")
    rows = []
    for sample_file in quantum:
        q, c = quantum[sample_file], classical[sample_file]
        if q["true_label"] != c["true_label"]:
            raise RuntimeError(f"True-label mismatch for {sample_file}.")
        if q["true_label"] == 0 and q["predicted_label"] == 1 and c["predicted_label"] == 0:
            rows.append({"sample_file": sample_file, "quantum_probability": q["vulnerable_probability"], "classical_probability": c["vulnerable_probability"]})
    rows.sort(key=lambda row: row["quantum_probability"] - row["classical_probability"], reverse=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    args.source_out.mkdir(parents=True, exist_ok=True)
    for path in args.source_out.glob("*.py"):
        path.unlink()
    for rank, row in enumerate(rows, start=1):
        source = args.source_root / row["sample_file"]
        target = args.source_out / f"{rank:02d}_{source.name}"
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    print(json.dumps({"quantum_only_false_positives": len(rows), "output": str(args.out), "source_out": str(args.source_out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
