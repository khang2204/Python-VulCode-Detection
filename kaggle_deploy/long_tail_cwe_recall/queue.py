#!/usr/bin/env python3
"""Compatibility entry point for local Long-tail inference evaluation."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVALUATOR = Path(__file__).resolve().parent / "evaluate_from_in_domain.py"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    subprocess.run(
        [
            sys.executable,
            str(EVALUATOR),
            "--runs-root",
            str(args.runs_root),
            "--metadata-root",
            str(ROOT / "CPG"),
            "--output",
            str(args.output),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
