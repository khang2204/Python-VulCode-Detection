#!/usr/bin/env python3
"""Create graph metadata and parse report for OWASP BenchmarkPython."""

from __future__ import annotations

import argparse
import ast
import csv
import json
from pathlib import Path


def load_expected(repo_root: Path) -> dict[str, dict]:
    expected_path = repo_root / "expectedresults-0.1.csv"
    if not expected_path.exists():
        return {}

    result = {}
    with expected_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            clean = {key.strip(): value for key, value in row.items() if key is not None}
            test_name = clean.get("# test name", "")
            if test_name:
                result[test_name] = {
                    "category": clean.get("category", ""),
                    "real_vulnerability": clean.get("real vulnerability", ""),
                    "cwe": clean.get("cwe", ""),
                }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default="data/BenchmarkPython")
    parser.add_argument("--metadata", default="CPG/BenchmarkPython/metadata.jsonl")
    parser.add_argument("--report", default="EDA/benchmarkpython_parse_report.json")
    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    metadata_path = Path(args.metadata)
    report_path = Path(args.report)
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    expected = load_expected(repo_root)
    stats = {
        "repo": "OWASP-Benchmark/BenchmarkPython",
        "python_files": 0,
        "parse_ok": 0,
        "parse_fail": 0,
        "testcode_files": 0,
        "metadata_with_expected_result": 0,
        "parse_errors": [],
    }

    with metadata_path.open("w", encoding="utf-8") as metadata_handle:
        for path in sorted(repo_root.rglob("*.py")):
            rel = path.relative_to(repo_root).as_posix()
            stats["python_files"] += 1
            try:
                ast.parse(path.read_text(encoding="utf-8", errors="replace"))
                parse_status = "ok"
                stats["parse_ok"] += 1
            except Exception as exc:
                parse_status = "fail"
                stats["parse_fail"] += 1
                if len(stats["parse_errors"]) < 20:
                    stats["parse_errors"].append(
                        {"file": rel, "error": f"{type(exc).__name__}: {exc}"}
                    )

            test_name = Path(rel).stem if rel.startswith("testcode/") else ""
            expected_result = expected.get(test_name, {})
            if rel.startswith("testcode/"):
                stats["testcode_files"] += 1
            if expected_result:
                stats["metadata_with_expected_result"] += 1

            metadata = {
                "sample_file": rel,
                "dataset": "OWASP-Benchmark/BenchmarkPython",
                "parse_status": parse_status,
                "test_name": test_name,
                **expected_result,
            }
            metadata_handle.write(json.dumps(metadata, ensure_ascii=False) + "\n")

    report_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(stats, indent=2, ensure_ascii=False))
    print(f"Wrote {metadata_path}")
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
