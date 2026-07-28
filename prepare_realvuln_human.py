#!/usr/bin/env python3
"""Prepare a conflict-free Python subset of RealVuln's human corpus.

RealVuln labels findings, not whole functions.  Each sample therefore contains
the labelled line range plus a fixed amount of surrounding source.  Only
manual-review findings from human-authored repositories pinned at the exact
ground-truth commit are accepted.  Identical source contexts with conflicting
binary labels are removed rather than resolved heuristically.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import textwrap
from collections import Counter, defaultdict
from pathlib import Path


def git_head(repo: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True,
        check=False,
        text=True,
    ).stdout.strip()


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark-root", type=Path, default=root / "external_datasets" / "RealVuln")
    parser.add_argument("--out-dir", type=Path, default=root / "CPG" / "RealVulnHuman")
    parser.add_argument("--context-lines", type=int, default=10)
    args = parser.parse_args()

    benchmark = args.benchmark_root.resolve()
    ground_truth = benchmark / "ground-truth"
    repos_root = benchmark / "repos"
    candidates: list[dict] = []
    excluded = Counter()
    unavailable_repos: list[dict] = []

    for gt_path in sorted(ground_truth.glob("*/ground-truth.json")):
        gt = json.loads(gt_path.read_text(encoding="utf-8"))
        if gt.get("authorship") != "human_authored":
            excluded["non_human_repository"] += len(gt.get("findings", []))
            continue
        repo = repos_root / gt_path.parent.name
        expected_sha = str(gt.get("commit_sha", ""))
        if not repo.is_dir() or git_head(repo) != expected_sha:
            unavailable_repos.append(
                {
                    "repo_id": gt.get("repo_id"),
                    "slug": gt_path.parent.name,
                    "expected_sha": expected_sha,
                    "repo_url": gt.get("repo_url"),
                    "findings": len(gt.get("findings", [])),
                }
            )
            excluded["repository_unavailable_at_pinned_commit"] += len(gt.get("findings", []))
            continue

        for finding in gt.get("findings", []):
            if finding.get("evidence", {}).get("source") != "manual_review":
                excluded["non_manual_label_source"] += 1
                continue
            relative_file = Path(str(finding.get("file", "")))
            if relative_file.suffix.lower() != ".py":
                excluded["non_python_source"] += 1
                continue
            source_path = repo / relative_file
            if not source_path.is_file():
                excluded["missing_source_file"] += 1
                continue
            lines = source_path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
            location = finding.get("location", {})
            start_line = int(location.get("start_line", 0))
            end_line = int(location.get("end_line", start_line))
            if start_line < 1 or end_line < start_line or start_line > len(lines):
                excluded["invalid_line_range"] += 1
                continue
            context_start = max(1, start_line - args.context_lines)
            context_end = min(len(lines), end_line + args.context_lines)
            source = textwrap.dedent("".join(lines[context_start - 1 : context_end])).strip() + "\n"
            if not source.strip():
                excluded["empty_context"] += 1
                continue
            source_hash = hashlib.sha256(source.encode()).hexdigest()
            candidates.append(
                {
                    "source": source,
                    "source_hash": source_hash,
                    "label": int(bool(finding.get("is_vulnerable"))),
                    "finding_id": finding.get("id"),
                    "repo_id": gt.get("repo_id"),
                    "repo_slug": gt_path.parent.name,
                    "commit_sha": expected_sha,
                    "original_file": relative_file.as_posix(),
                    "original_start_line": start_line,
                    "original_end_line": end_line,
                    "context_start_line": context_start,
                    "context_end_line": context_end,
                    "function": location.get("function"),
                    "primary_cwe": finding.get("primary_cwe") or "CWE-UNKNOWN",
                    "vulnerability_class": finding.get("vulnerability_class"),
                    "evidence_description": finding.get("evidence", {}).get("description"),
                }
            )

    by_source: dict[str, list[dict]] = defaultdict(list)
    for record in candidates:
        by_source[record["source_hash"]].append(record)

    selected: list[dict] = []
    conflicting_hashes: list[str] = []
    for source_hash, group in sorted(by_source.items()):
        labels = {record["label"] for record in group}
        if len(labels) != 1:
            conflicting_hashes.append(source_hash)
            excluded["conflicting_binary_labels"] += len(group)
            continue
        representative = group[0].copy()
        representative["finding_ids"] = sorted({str(record["finding_id"]) for record in group})
        representative["primary_cwes"] = sorted({str(record["primary_cwe"]) for record in group})
        representative["merged_duplicate_findings"] = len(group)
        selected.append(representative)
        excluded["same_label_duplicate_context"] += len(group) - 1

    out_dir = args.out_dir.resolve()
    source_root = out_dir / "source" / "realvuln_human"
    if source_root.exists():
        shutil.rmtree(source_root)
    source_root.mkdir(parents=True, exist_ok=True)
    metadata: list[dict] = []
    for record in selected:
        filename = f"realvuln_human_{record['source_hash'][:20]}.py"
        (source_root / filename).write_text(record["source"], encoding="utf-8")
        metadata.append(
            {
                "sample_file": f"realvuln_human/{filename}",
                "pair_id": record["source_hash"],
                "version": "finding_context",
                "real_vulnerability": "true" if record["label"] else "false",
                "cwe": record["primary_cwe"] if record["label"] else "BENIGN",
                "source_cwe": record["primary_cwe"],
                **{key: value for key, value in record.items() if key != "source"},
            }
        )
    metadata_path = out_dir / "metadata.jsonl"
    metadata_path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in metadata), encoding="utf-8")
    report = {
        "dataset": "RealVulnHuman",
        "benchmark_version": "2.0.0",
        "selection": "human_authored repositories; manual_review findings; Python files; exact pinned commits",
        "representation": f"finding line range with +/-{args.context_lines} source lines",
        "raw_candidate_findings": len(candidates),
        "selected_unique_contexts": len(metadata),
        "binary_counts": {
            "benign": sum(row["real_vulnerability"] == "false" for row in metadata),
            "vulnerable": sum(row["real_vulnerability"] == "true" for row in metadata),
        },
        "excluded": dict(sorted(excluded.items())),
        "unavailable_repositories": unavailable_repos,
        "conflicting_source_hashes": conflicting_hashes,
        "context_lines": args.context_lines,
        "metadata": str(metadata_path),
        "source_root": str(source_root),
    }
    (out_dir / "prepare_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
