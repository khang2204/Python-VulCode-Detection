#!/usr/bin/env python3
"""Export every Joern-constructible VUDENC block as a binary PyG graph.

The source preparation deliberately keeps all labelled VUDENC blocks. This
script records the precise raw-to-CPG-to-PyG retention count, making Joern the
only parser gate.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from collections import Counter
from pathlib import Path

from export_benchmarkpython_pyg import EDGE_TYPE_TO_ID, FEATURE_DIM, build_pyg_dataset, run_joern_export


def load_metadata(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            if row.get("sample_file", "").startswith("vudenc/") and row.get("real_vulnerability") in {"true", "false"}:
                rows.append(row)
    if not rows:
        raise RuntimeError("No labelled VUDENC metadata records found.")
    return sorted(rows, key=lambda item: item["sample_file"])


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpg", type=Path, default=root / "CPG" / "Vudenc" / "cpg.bin")
    parser.add_argument("--metadata", type=Path, default=root / "CPG" / "Vudenc" / "metadata.jsonl")
    parser.add_argument("--out-dir", type=Path, default=root / "artifacts" / "vudenc_binary_pyg")
    parser.add_argument("--joern", type=Path, default=Path("/home/khang/bin/joern/joern-cli/joern"))
    args = parser.parse_args()
    # Resolve before entering the temporary Joern working directory.  Resolving
    # a relative CPG path after chdir would point into that temporary folder.
    cpg_path = args.cpg.resolve()
    metadata_path = args.metadata.resolve()
    joern_path = args.joern.resolve()
    for path, name in ((args.cpg, "CPG"), (args.metadata, "metadata"), (args.joern, "Joern CLI")):
        if not path.is_file():
            raise SystemExit(f"Missing {name}: {path}")

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    selected = load_metadata(metadata_path)
    selected_by_file = {item["sample_file"]: item for item in selected}
    (out_dir / "selected_files.txt").write_text("".join(f"{item['sample_file']}\n" for item in selected), encoding="utf-8")
    label_map = {"benign": 0, "vulnerable": 1}
    (out_dir / "label_map.json").write_text(json.dumps(label_map, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    raw_graphs = out_dir / "joern_graphs.jsonl"
    log = out_dir / "joern_export.log"
    scala_script = root / "scripts" / "export_benchmarkpython_cpg.sc"
    with tempfile.TemporaryDirectory(prefix="pagvul-joern-", dir=out_dir) as workdir:
        previous = Path.cwd()
        try:
            os.chdir(workdir)
            run_joern_export(joern_path, cpg_path, scala_script.resolve(), out_dir / "selected_files.txt", raw_graphs, log)
        finally:
            os.chdir(previous)

    graphs, skipped = build_pyg_dataset(raw_graphs, selected_by_file)
    import torch

    dataset_path = out_dir / "vudenc_binary_graphs.pt"
    torch.save(graphs, dataset_path)
    exported_files = {str(graph.sample_file) for graph in graphs}
    missing_from_cpg = sorted(set(selected_by_file) - exported_files)
    edge_counts = Counter()
    for graph in graphs:
        for edge_type in graph.edge_type.tolist():
            edge_counts[next(name for name, identifier in EDGE_TYPE_TO_ID.items() if identifier == edge_type)] += 1
    report = {
        "dataset": "VUDENC",
        "representation": "raw_statement_context_blocks_joern_filtered",
        "raw_labelled_samples": len(selected),
        "exported_graphs": len(graphs),
        "not_exported_by_joern": len(missing_from_cpg),
        "not_exported_preview": missing_from_cpg[:100],
        "skipped_graphs": skipped,
        "labels": label_map,
        "binary_counts": {
            "benign": sum(int(graph.y.item()) == 0 for graph in graphs),
            "vulnerable": sum(int(graph.y.item()) == 1 for graph in graphs),
        },
        "vulnerable_counts_by_cwe": dict(sorted(Counter(str(graph.cwe) for graph in graphs if int(graph.y.item()) == 1).items())),
        "feature_dim": FEATURE_DIM,
        "edge_type_to_id": EDGE_TYPE_TO_ID,
        "edge_counts_with_reverse_edges": dict(sorted(edge_counts.items())),
        "dataset_path": str(dataset_path),
        "raw_joern_graphs": str(raw_graphs),
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
