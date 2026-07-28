#!/usr/bin/env python3
"""Create binary PAG-Vul-ready graphs from the BenchmarkPython Joern CPG.

Every labelled BenchmarkPython test case is exported.  ``Data.y`` is the
ground-truth binary target (0 = benign, 1 = vulnerable); ``Data.cwe`` remains
attached as metadata so a later prototype bank can be CWE-aware without
treating Benign as a CWE class.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


EDGE_TYPE_TO_ID = {"AST": 0, "CFG": 1, "REACHING_DEF": 2}
FEATURE_DIM = 128
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z_0-9]*|\d+|[^\s]")


def stable_bucket(value: str, buckets: int, namespace: bytes) -> tuple[int, float]:
    digest = hashlib.blake2b(value.encode("utf-8", errors="replace"), digest_size=8, person=namespace).digest()
    return int.from_bytes(digest[:4], "little") % buckets, 1.0 if digest[4] & 1 else -1.0


def node_feature(node: dict[str, Any]) -> list[float]:
    """A deterministic 128-dim feature: node-type one-hot hash + code-token hash."""
    feature = [0.0] * FEATURE_DIM
    label_bucket, _ = stable_bucket(str(node["label"]), 64, b"pagvul-lbl")
    feature[label_bucket] = 1.0
    for token in TOKEN_RE.findall(str(node.get("code", "")))[:64]:
        token_bucket, sign = stable_bucket(token, 64, b"pagvul-tok")
        feature[64 + token_bucket] += sign
    return feature


def load_selected_metadata(metadata_path: Path, limit: int | None) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    with metadata_path.open(encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            if not (
                item.get("parse_status") == "ok"
                and item.get("sample_file", "").startswith("testcode/")
                and item.get("real_vulnerability") in {"true", "false"}
                and item.get("cwe")
            ):
                continue
            selected.append(item)
    selected.sort(key=lambda item: item["sample_file"])
    if limit is not None:
        selected = selected[:limit]
    if not selected:
        raise RuntimeError("No parseable BenchmarkPython test samples with labels were selected.")
    return selected


def run_joern_export(
    joern: Path, cpg: Path, scala_script: Path, selected_files: Path, raw_graphs: Path, log: Path
) -> None:
    command = [
        str(joern),
        str(cpg),
        "--script",
        str(scala_script),
        "--param",
        f"files={selected_files}",
        "--param",
        f"output={raw_graphs}",
    ]
    with log.open("w", encoding="utf-8") as log_handle:
        process = subprocess.run(command, stdout=log_handle, stderr=subprocess.STDOUT, text=True, check=False)
    if process.returncode != 0:
        raise RuntimeError(f"Joern export failed (exit {process.returncode}); see {log}")
    if not raw_graphs.is_file() or raw_graphs.stat().st_size == 0:
        raise RuntimeError("Joern completed without writing any graph records.")


def build_pyg_dataset(raw_graphs: Path, selected_by_file: dict[str, dict[str, str]]):
    try:
        import torch
        from torch_geometric.data import Data
    except ImportError as error:  # pragma: no cover - exercised only without optional ML deps
        raise RuntimeError(
            "PyTorch and torch-geometric are required for step 7. "
            "Install them in the active environment, then re-run this script."
        ) from error

    graphs = []
    skipped: list[dict[str, str]] = []
    with raw_graphs.open(encoding="utf-8") as handle:
        for line in handle:
            raw = json.loads(line)
            metadata = selected_by_file.get(raw["sample_file"])
            if metadata is None:
                continue
            nodes = raw["nodes"]
            if not nodes:
                skipped.append({"sample_file": raw["sample_file"], "reason": "no_nodes"})
                continue
            local_id = {node["id"]: index for index, node in enumerate(nodes)}
            edges: list[tuple[int, int, int]] = []
            for source, destination, edge_type in raw["edges"]:
                if source not in local_id or destination not in local_id:
                    continue
                type_id = EDGE_TYPE_TO_ID[edge_type]
                edges.append((local_id[source], local_id[destination], type_id))
                edges.append((local_id[destination], local_id[source], type_id))
            if edges:
                edge_index = torch.tensor([[edge[0] for edge in edges], [edge[1] for edge in edges]], dtype=torch.long)
                edge_type = torch.tensor([edge[2] for edge in edges], dtype=torch.long)
            else:
                edge_index = torch.empty((2, 0), dtype=torch.long)
                edge_type = torch.empty((0,), dtype=torch.long)
            graph = Data(
                x=torch.tensor([node_feature(node) for node in nodes], dtype=torch.float32),
                edge_index=edge_index,
                edge_type=edge_type,
                y=torch.tensor([int(metadata["real_vulnerability"] == "true")], dtype=torch.long),
            )
            graph.sample_file = metadata["sample_file"]
            graph.cwe = metadata["cwe"]
            graph.is_vulnerable = metadata["real_vulnerability"] == "true"
            graph.line_numbers = torch.tensor(
                [node["line"] if node["line"] is not None else -1 for node in nodes], dtype=torch.long
            )
            graphs.append(graph)
    if not graphs:
        raise RuntimeError("No PyG graphs were created from the Joern export.")
    return graphs, skipped


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpg", type=Path, default=root / "CPG" / "BenchmarkPython" / "cpg.bin")
    parser.add_argument("--metadata", type=Path, default=root / "CPG" / "BenchmarkPython" / "metadata.jsonl")
    parser.add_argument("--out-dir", type=Path, default=root / "artifacts" / "benchmarkpython_binary_pyg")
    parser.add_argument("--joern", type=Path, default=Path("/home/khang/bin/joern/joern-cli/joern"))
    parser.add_argument("--limit", type=int, help="Export only the first N selected samples (for smoke tests).")
    args = parser.parse_args()

    if args.limit is not None and args.limit <= 0:
        raise SystemExit("--limit must be positive")
    for path, name in ((args.cpg, "CPG"), (args.metadata, "metadata"), (args.joern, "Joern CLI")):
        if not path.is_file():
            raise SystemExit(f"Missing {name}: {path}")

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    # Resolve these before entering Joern's temporary working directory.
    # Otherwise a caller-provided relative --cpg/--metadata path would be
    # interpreted relative to that temporary directory.
    cpg_path = args.cpg.resolve()
    metadata_path = args.metadata.resolve()
    joern_path = args.joern.resolve()
    selected = load_selected_metadata(metadata_path, args.limit)
    selected_by_file = {item["sample_file"]: item for item in selected}
    selected_files = out_dir / "selected_files.txt"
    selected_files.write_text("".join(f"{item['sample_file']}\n" for item in selected), encoding="utf-8")
    label_map = {"benign": 0, "vulnerable": 1}
    (out_dir / "label_map.json").write_text(json.dumps(label_map, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    raw_graphs = out_dir / "joern_graphs.jsonl"
    log = out_dir / "joern_export.log"
    scala_script = root / "scripts" / "export_benchmarkpython_cpg.sc"
    with tempfile.TemporaryDirectory(prefix="pagvul-joern-", dir=out_dir) as joern_workdir:
        previous_cwd = Path.cwd()
        try:
            # Joern writes a temporary workspace next to its working directory.
            import os

            os.chdir(joern_workdir)
            run_joern_export(joern_path, cpg_path, scala_script.resolve(), selected_files, raw_graphs, log)
        finally:
            os.chdir(previous_cwd)

    graphs, skipped = build_pyg_dataset(raw_graphs, selected_by_file)
    import torch

    dataset_path = out_dir / "benchmarkpython_binary_graphs.pt"
    torch.save(graphs, dataset_path)
    edge_counts = Counter()
    for graph in graphs:
        for edge_type in graph.edge_type.tolist():
            edge_counts[next(name for name, identifier in EDGE_TYPE_TO_ID.items() if identifier == edge_type)] += 1
    report = {
        "selected_samples": len(selected),
        "exported_graphs": len(graphs),
        "skipped_graphs": skipped,
        "labels": label_map,
        "binary_counts": {
            "benign": sum(item["real_vulnerability"] == "false" for item in selected),
            "vulnerable": sum(item["real_vulnerability"] == "true" for item in selected),
        },
        "vulnerable_counts_by_cwe": {
            cwe: sum(item["cwe"] == cwe and item["real_vulnerability"] == "true" for item in selected)
            for cwe in sorted({item["cwe"] for item in selected}, key=int)
        },
        "feature_dim": FEATURE_DIM,
        "edge_type_to_id": EDGE_TYPE_TO_ID,
        "edge_counts_with_reverse_edges": dict(sorted(edge_counts.items())),
        "dataset": str(dataset_path),
        "raw_joern_graphs": str(raw_graphs),
    }
    (out_dir / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
