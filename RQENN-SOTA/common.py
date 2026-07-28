"""Shared fixed-split data and metrics for the standalone SOTA runners."""
from __future__ import annotations

import io
import json
import keyword
import random
import token
import tokenize
from collections import Counter
from pathlib import Path

import torch

DATASETS = ("benchmarkpython", "vudenc", "realvuln_human")
SEEDS = (101, 202, 303)
SPLIT_SEED = 101
GRAPH_PATHS = {
    "benchmarkpython": "artifacts/benchmarkpython_binary_pyg/benchmarkpython_binary_graphs.pt",
    "vudenc": "artifacts/vudenc_binary_pyg/vudenc_binary_graphs.pt",
    "realvuln_human": "artifacts/realvuln_human_binary_pyg/realvuln_human_binary_graphs.pt",
}
SOURCE_ROOTS = {
    "benchmarkpython": "data/BenchmarkPython",
    "vudenc": "CPG/Vudenc/source",
    "realvuln_human": "CPG/RealVulnHuman/source",
}


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def normalized_tokens(source: str) -> list[str]:
    """Tokenize Python and normalize identifiers without using labels."""
    try:
        stream = [
            item
            for item in tokenize.generate_tokens(io.StringIO(source).readline)
            if item.type not in {
                token.ENDMARKER, token.ENCODING, token.INDENT, token.DEDENT,
                token.NEWLINE, tokenize.NL, tokenize.COMMENT,
            }
        ]
        output: list[str] = []
        variables: dict[str, str] = {}
        functions: dict[str, str] = {}
        for index, item in enumerate(stream):
            value = item.string
            if item.type == token.NUMBER:
                value = "<NUM>"
            elif item.type == token.STRING:
                value = "<STR>"
            elif item.type == token.NAME:
                if keyword.iskeyword(value):
                    value = f"KW_{value}"
                else:
                    previous = stream[index - 1].string if index else ""
                    following = stream[index + 1].string if index + 1 < len(stream) else ""
                    is_function = previous == "def" or following == "("
                    table = functions if is_function else variables
                    prefix = "FUN" if is_function else "VAR"
                    table.setdefault(value, f"{prefix}{len(table) + 1}")
                    value = table[value]
            output.append(value)
        return output
    except (IndentationError, SyntaxError, tokenize.TokenError):
        return source.replace("\n", " ").split()


def load_records(repo_root: Path, dataset: str, cache_dir: Path) -> list[dict]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache = cache_dir / f"{dataset}_records_v3.pt"
    if cache.is_file():
        return torch.load(cache, map_location="cpu", weights_only=False)
    graphs = torch.load(repo_root / GRAPH_PATHS[dataset], map_location="cpu", weights_only=False)
    records = []
    for graph in graphs:
        sample_file = str(graph.sample_file)
        source_path = repo_root / SOURCE_ROOTS[dataset] / sample_file
        source = source_path.read_text(encoding="utf-8", errors="replace")
        records.append({
            "sample_file": sample_file,
            "label": int(graph.y.item()),
            "cwe": str(getattr(graph, "cwe", "UNKNOWN")),
            "source": source,
            "tokens": normalized_tokens(source),
        })
    torch.save(records, cache)
    return records


def fixed_manifest(records: list[dict], cache_dir: Path, dataset: str) -> dict:
    path = cache_dir / f"{dataset}_split_seed_{SPLIT_SEED}.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    groups = {0: [], 1: []}
    for index, record in enumerate(records):
        groups[record["label"]].append(index)
    generator = torch.Generator().manual_seed(SPLIT_SEED)
    result = {"train": [], "validation": [], "test": []}
    for label in (0, 1):
        members = groups[label]
        order = torch.randperm(len(members), generator=generator).tolist()
        shuffled = [members[index] for index in order]
        n_validation = max(1, round(0.15 * len(shuffled)))
        n_test = max(1, round(0.15 * len(shuffled)))
        n_train = len(shuffled) - n_validation - n_test
        result["train"].extend(shuffled[:n_train])
        result["validation"].extend(shuffled[n_train:n_train + n_validation])
        result["test"].extend(shuffled[n_train + n_validation:])
    payload = {
        "split_seed": SPLIT_SEED,
        "ratios": {"train": 0.70, "validation": 0.15, "test": 0.15},
        **result,
        "sample_files": {
            part: [records[index]["sample_file"] for index in result[part]]
            for part in result
        },
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def ten_percent_indices(records: list[dict], train_indices: list[int], seed: int) -> list[int]:
    """Sample 10% within binary/CWE strata from fixed training only."""
    groups: dict[tuple[int, str], list[int]] = {}
    for index in train_indices:
        record = records[index]
        key = (record["label"], "BENIGN" if record["label"] == 0 else record["cwe"])
        groups.setdefault(key, []).append(index)
    generator = torch.Generator().manual_seed(seed)
    selected = []
    for key in sorted(groups):
        members = sorted(groups[key], key=lambda i: records[i]["sample_file"])
        amount = min(len(members), max(1, round(0.1 * len(members))))
        order = torch.randperm(len(members), generator=generator)[:amount].tolist()
        selected.extend(members[offset] for offset in order)
    return sorted(selected)


def rare_cwes(records: list[dict], train_indices: list[int]) -> set[str]:
    counts = Counter(
        records[index]["cwe"]
        for index in train_indices
        if records[index]["label"] == 1
    )
    if not counts:
        return set()
    cutoff = sorted(counts.values())[(len(counts) - 1) // 2]
    return {name for name, count in counts.items() if count <= cutoff}


def binary_metrics(logits: torch.Tensor, labels: torch.Tensor) -> dict[str, float]:
    predictions = logits.argmax(dim=-1)
    tp = int(((predictions == 1) & (labels == 1)).sum())
    tn = int(((predictions == 0) & (labels == 0)).sum())
    fp = int(((predictions == 1) & (labels == 0)).sum())
    fn = int(((predictions == 0) & (labels == 1)).sum())
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    return {
        "accuracy": (tp + tn) / max(1, len(labels)),
        "balanced_accuracy": 0.5 * (
            tp / max(1, tp + fn) + tn / max(1, tn + fp)
        ),
        "precision": precision,
        "recall": recall,
        "f1": 2 * precision * recall / max(1e-12, precision + recall),
        "vulnerable_recall": recall,
    }


def manifest_hash(records: list[dict], manifest: dict) -> str:
    import hashlib
    value = {
        part: [records[index]["sample_file"] for index in manifest[part]]
        for part in ("train", "validation", "test")
    }
    return hashlib.sha256(
        json.dumps(value, separators=(",", ":")).encode()
    ).hexdigest()
