#!/usr/bin/env python3
"""Build the Joern CPG for OWASP BenchmarkPython."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path


def run_and_log(command: list[str], log_path: Path) -> None:
    with log_path.open("w", encoding="utf-8") as log_handle:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        for line in process.stdout:
            print(line, end="")
            log_handle.write(line)
        if process.wait() != 0:
            raise SystemExit(process.returncode)


def load_main(script_path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load helper script: {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main


def main() -> int:
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=str(root / "data" / "BenchmarkPython"))
    parser.add_argument("--out-dir", default=str(root / "CPG" / "BenchmarkPython"))
    parser.add_argument("--joern-parse", default=os.environ.get("JOERN_PARSE", "joern-parse"))
    args = parser.parse_args()

    repo_root = Path(args.repo_root)
    out_dir = Path(args.out_dir)
    prepare_metadata_main = load_main(
        repo_root / "prepare_benchmarkpython_metadata.py",
        "prepare_benchmarkpython_metadata",
    )
    metadata = out_dir / "metadata.jsonl"
    parse_report = root / "EDA" / "benchmarkpython_parse_report.json"
    cpg = out_dir / "cpg.bin"
    log = out_dir / "joern-parse.log"
    report_path = out_dir / "report.json"

    out_dir.mkdir(parents=True, exist_ok=True)
    parse_report.parent.mkdir(parents=True, exist_ok=True)

    old_argv = sys.argv
    try:
        sys.argv = [
            "prepare_benchmarkpython_metadata.py",
            "--repo-root",
            str(repo_root),
            "--metadata",
            str(metadata),
            "--report",
            str(parse_report),
        ]
        prepare_metadata_main()
    finally:
        sys.argv = old_argv

    cpg.unlink(missing_ok=True)
    log.unlink(missing_ok=True)
    run_and_log(
        [args.joern_parse, str(repo_root), "--language", "PYTHONSRC", "--output", str(cpg)],
        log,
    )
    if not cpg.is_file() or cpg.stat().st_size == 0:
        raise SystemExit(f"ERROR: Joern did not create a non-empty CPG at {cpg}")

    parse_data = json.loads(parse_report.read_text(encoding="utf-8"))
    report = {
        "dataset": "OWASP-Benchmark/BenchmarkPython",
        "python_files": parse_data.get("python_files"),
        "parse_ok": parse_data.get("parse_ok"),
        "parse_fail": parse_data.get("parse_fail"),
        "testcode_files": parse_data.get("testcode_files"),
        "metadata_with_expected_result": parse_data.get("metadata_with_expected_result"),
        "metadata": str(metadata),
        "cpg": str(cpg),
        "log": str(log),
        "cpg_bytes": cpg.stat().st_size,
    }
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
