"""Fixed-split Python token data for the faithful SOTA adaptations."""
from __future__ import annotations

import io
import json
import keyword
import token
import tokenize
from collections import Counter
from pathlib import Path

import torch
from torch.utils.data import Dataset


PAD = "<PAD>"
UNK = "<UNK>"
VOCAB_SIZE = 128
MAX_LEN = 100
CACHE_VERSION = 3

DATASET_GRAPH_PATHS = {
    "benchmarkpython": "artifacts/benchmarkpython_binary_pyg/benchmarkpython_binary_graphs.pt",
    "vudenc": "artifacts/vudenc_binary_pyg/vudenc_binary_graphs.pt",
    "realvuln_human": "artifacts/realvuln_human_binary_pyg/realvuln_human_binary_graphs.pt",
}


def resolve_source(repo_root: Path, dataset: str, sample_file: str) -> Path:
    roots = {
        "benchmarkpython": repo_root / "data" / "BenchmarkPython",
        "vudenc": repo_root / "CPG" / "Vudenc" / "source",
        "realvuln_human": repo_root / "CPG" / "RealVulnHuman" / "source",
    }
    path = roots[dataset] / sample_file
    if not path.is_file():
        raise FileNotFoundError(f"Missing source for {dataset}: {path}")
    return path


def python_tokens(source: str) -> list[str]:
    """Tokenize and normalize Python source without labels or graph embeddings.

    The source papers normalize variable and function identifiers inside code
    gadgets.  Python snippets are adapted with deterministic VAR/FUN symbols.
    """
    try:
        stream = [
            item
            for item in tokenize.generate_tokens(io.StringIO(source).readline)
            if item.type
            not in {
                token.ENDMARKER,
                token.ENCODING,
                token.INDENT,
                token.DEDENT,
                token.NEWLINE,
                tokenize.NL,
                tokenize.COMMENT,
            }
        ]
        result: list[str] = []
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
                    mapping = functions if is_function else variables
                    prefix = "FUN" if is_function else "VAR"
                    if value not in mapping:
                        mapping[value] = f"{prefix}{len(mapping) + 1}"
                    value = mapping[value]
            result.append(value)
    except (IndentationError, SyntaxError, tokenize.TokenError):
        # Some vulnerability snippets are intentionally incomplete.
        result = source.replace("\n", " ").split()
    return result


def stratified_manifest(items: list[dict], split_seed: int = 101) -> dict:
    """Reproduce the Our-pipeline fixed stratified split exactly."""
    groups: dict[int, list[int]] = {0: [], 1: []}
    for index, item in enumerate(items):
        groups[item["label"]].append(index)
    generator = torch.Generator().manual_seed(split_seed)
    result = {"train": [], "validation": [], "test": []}
    for label in sorted(groups):
        indices = groups[label]
        order = torch.randperm(len(indices), generator=generator).tolist()
        shuffled = [indices[offset] for offset in order]
        n_validation = max(1, round(0.15 * len(indices)))
        n_test = max(1, round(0.15 * len(indices)))
        n_train = len(indices) - n_validation - n_test
        result["train"].extend(shuffled[:n_train])
        result["validation"].extend(shuffled[n_train : n_train + n_validation])
        result["test"].extend(shuffled[n_train + n_validation :])
    return {
        "split_seed": split_seed,
        "ratios": {"train": 0.70, "validation": 0.15, "test": 0.15},
        **result,
    }


def build_records(repo_root: Path, dataset: str) -> list[dict]:
    graph_path = repo_root / DATASET_GRAPH_PATHS[dataset]
    graphs = torch.load(graph_path, map_location="cpu", weights_only=False)
    records = []
    for graph in graphs:
        sample_file = str(graph.sample_file)
        path = resolve_source(repo_root, dataset, sample_file)
        source = path.read_text(encoding="utf-8", errors="replace")
        records.append(
            {
                "sample_file": sample_file,
                "label": int(graph.y.item()),
                "cwe": str(getattr(graph, "cwe", "UNKNOWN")),
                "tokens": python_tokens(source),
            }
        )
    return records


def build_vocab(records: list[dict], train_indices: list[int]) -> dict[str, int]:
    counts = Counter(
        value
        for index in train_indices
        for value in records[index]["tokens"]
    )
    vocab = {PAD: 0, UNK: 1}
    for value, _ in counts.most_common(VOCAB_SIZE - len(vocab)):
        vocab[value] = len(vocab)
    return vocab


class TokenDataset(Dataset):
    def __init__(
        self,
        records: list[dict],
        indices: list[int],
        vocab: dict[str, int],
        max_len: int = MAX_LEN,
    ):
        self.records = records
        self.indices = indices
        self.vocab = vocab
        self.max_len = max_len

    def __len__(self) -> int:
        return len(self.indices)

    def __getitem__(self, offset: int) -> tuple[torch.Tensor, torch.Tensor]:
        record = self.records[self.indices[offset]]
        values = [self.vocab.get(value, 1) for value in record["tokens"][: self.max_len]]
        values.extend([0] * (self.max_len - len(values)))
        return torch.tensor(values, dtype=torch.long), torch.tensor(
            record["label"], dtype=torch.long
        )


def prepare_dataset(
    repo_root: Path,
    dataset: str,
    cache_dir: Path,
    split_seed: int = 101,
) -> tuple[dict[str, TokenDataset], dict, dict]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"{dataset}_tokens_v{CACHE_VERSION}.pt"
    if cache_path.exists():
        records = torch.load(cache_path, map_location="cpu", weights_only=False)
    else:
        records = build_records(repo_root, dataset)
        torch.save(records, cache_path)

    manifest_path = cache_dir / f"{dataset}_split_v{CACHE_VERSION}_{split_seed}.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
    else:
        manifest = stratified_manifest(records, split_seed)
        serializable = {
            **manifest,
            "sample_files": {
                part: [records[index]["sample_file"] for index in manifest[part]]
                for part in ("train", "validation", "test")
            },
        }
        manifest_path.write_text(json.dumps(serializable, indent=2) + "\n")

    vocab_path = cache_dir / f"{dataset}_vocab_v{CACHE_VERSION}_split_{split_seed}.json"
    if vocab_path.exists():
        vocab = json.loads(vocab_path.read_text())
    else:
        vocab = build_vocab(records, manifest["train"])
        vocab_path.write_text(json.dumps(vocab, indent=2, ensure_ascii=False) + "\n")

    datasets = {
        part: TokenDataset(records, manifest[part], vocab)
        for part in ("train", "validation", "test")
    }
    return datasets, manifest, vocab
