#!/usr/bin/env python3
"""Export the prepared RealVuln Human finding contexts to a PyG dataset."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from collections import Counter
from pathlib import Path

from export_benchmarkpython_pyg import EDGE_TYPE_TO_ID, FEATURE_DIM, build_pyg_dataset, run_joern_export


def load_metadata(path: Path) -> list[dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = [
        row
        for row in rows
        if row.get("sample_file", "").startswith("realvuln_human/")
        and row.get("real_vulnerability") in {"true", "false"}
    ]
    if not rows:
        raise RuntimeError("No labelled RealVuln Human metadata records found.")
    return sorted(rows, key=lambda row: row["sample_file"])


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpg", type=Path, default=root / "CPG" / "RealVulnHuman" / "cpg.bin")
    parser.add_argument("--metadata", type=Path, default=root / "CPG" / "RealVulnHuman" / "metadata.jsonl")
    parser.add_argument("--out-dir", type=Path, default=root / "artifacts" / "realvuln_human_binary_pyg")
    parser.add_argument("--joern", type=Path, default=Path("/home/khang/bin/joern/joern-cli/joern"))
    args = parser.parse_args()
    cpg_path = args.cpg.resolve()
    metadata_path = args.metadata.resolve()
    joern_path = args.joern.resolve()
    for path, name in ((cpg_path, "CPG"), (metadata_path, "metadata"), (joern_path, "Joern CLI")):
        if not path.is_file():
            raise SystemExit(f"Missing {name}: {path}")

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    selected = load_metadata(metadata_path)
    selected_by_file = {row["sample_file"]: row for row in selected}
    selected_files = out_dir / "selected_files.txt"
    selected_files.write_text("".join(f"{row['sample_file']}\n" for row in selected), encoding="utf-8")
    label_map = {"benign": 0, "vulnerable": 1}
    (out_dir / "label_map.json").write_text(json.dumps(label_map, indent=2) + "\n", encoding="utf-8")

    raw_graphs = out_dir / "joern_graphs.jsonl"
    log = out_dir / "joern_export.log"
    scala_script = (root / "scripts" / "export_benchmarkpython_cpg.sc").resolve()
    with tempfile.TemporaryDirectory(prefix="realvuln-human-joern-", dir=out_dir) as workdir:
        previous = Path.cwd()
        try:
            os.chdir(workdir)
            run_joern_export(joern_path, cpg_path, scala_script, selected_files, raw_graphs, log)
        finally:
            os.chdir(previous)

    graphs, skipped = build_pyg_dataset(raw_graphs, selected_by_file)
    import torch

    dataset_path = out_dir / "realvuln_human_binary_graphs.pt"
    torch.save(graphs, dataset_path)
    exported_files = {str(graph.sample_file) for graph in graphs}
    missing = sorted(set(selected_by_file) - exported_files)
    edge_counts = Counter()
    edge_names = {identifier: name for name, identifier in EDGE_TYPE_TO_ID.items()}
    for graph in graphs:
        edge_counts.update(edge_names[int(edge_type)] for edge_type in graph.edge_type.tolist())
    report = {
        "dataset": "RealVulnHuman",
        "representation": "manual finding contexts, human-authored repositories, Joern-filtered",
        "prepared_contexts": len(selected),
        "exported_graphs": len(graphs),
        "not_exported_by_joern": len(missing),
        "not_exported_preview": missing[:100],
        "skipped_graphs": skipped,
        "binary_counts": {
            "benign": sum(int(graph.y.item()) == 0 for graph in graphs),
            "vulnerable": sum(int(graph.y.item()) == 1 for graph in graphs),
        },
        "vulnerable_counts_by_cwe": dict(
            sorted(Counter(str(graph.cwe) for graph in graphs if int(graph.y.item()) == 1).items())
        ),
        "feature_dim": FEATURE_DIM,
        "edge_type_to_id": EDGE_TYPE_TO_ID,
        "edge_counts_with_reverse_edges": dict(sorted(edge_counts.items())),
        "dataset_path": str(dataset_path),
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
