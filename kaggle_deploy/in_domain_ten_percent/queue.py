#!/usr/bin/env python3
"""Run and collect matched 10%-train in-domain sample-efficiency replicates."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KAGGLE = ROOT / '.venv/bin/kaggle'
SUBMIT = Path(__file__).resolve().parent / 'submit.py'
KERNEL = 'khangtrn2/pag-vul-ten-percent-in-domain'
OUT = ROOT / 'experiments/sample_efficiency_ten_percent/replicates'


def run(*args: str) -> None:
    print('+', ' '.join(args), flush=True)
    subprocess.run(args, check=True)


def status() -> str:
    result = subprocess.run(
        [str(KAGGLE), 'kernels', 'status', KERNEL], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True,
    )
    print(result.stdout.strip(), flush=True)
    return result.stdout


def collect(seed: int) -> None:
    target = OUT / f'seed_{seed}' / 'raw'
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)
    for _ in range(8):
        run(str(KAGGLE), 'kernels', 'output', KERNEL, '-p', str(target))
        if (target / 'ten_percent_results/report.json').is_file():
            return
        print('Report is not mounted yet; retrying in 30 seconds.', flush=True)
        time.sleep(30)
    raise RuntimeError(f'Missing report for seed {seed}: {target}')


def summarize(seeds: list[int]) -> None:
    rows: dict[str, dict[str, dict[str, list[float]]]] = {}
    for seed in seeds:
        report = OUT / f'seed_{seed}' / 'raw/ten_percent_results/report.json'
        if not report.is_file():
            continue
        summary = json.loads(report.read_text())['summary']
        for dataset, fractions in summary.items():
            for method, metrics in fractions['0.1'].items():
                bucket = rows.setdefault(dataset, {}).setdefault(method, {})
                for metric, value in metrics.items():
                    bucket.setdefault(metric, []).append(value)
    result = {'runs': len(seeds), 'fraction': 0.1, 'datasets': {}}
    for dataset, methods in rows.items():
        result['datasets'][dataset] = {}
        for method, metrics in methods.items():
            result['datasets'][dataset][method] = {
                metric: {
                    'mean': sum(values) / len(values),
                    'std': (sum((v - sum(values) / len(values)) ** 2 for v in values) / len(values)) ** .5,
                    'n': len(values),
                }
                for metric, values in metrics.items()
            }
    dest = ROOT / 'experiments/sample_efficiency_ten_percent/summary_10pct.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2) + '\n')
    print(f'Wrote {dest}', flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--seeds', nargs='+', type=int, default=[101, 202, 303])
    parser.add_argument('--datasets', nargs='+', default=['benchmarkpython', 'vudenc'])
    args = parser.parse_args()
    for seed in args.seeds:
        run(str(ROOT / '.venv/bin/python'), str(SUBMIT), '--seed', str(seed), '--datasets', *args.datasets, '--submit')
        seen_running = False
        while True:
            current = status()
            if 'KernelWorkerStatus.RUNNING' in current:
                seen_running = True
            elif 'KernelWorkerStatus.COMPLETE' in current and seen_running:
                collect(seed)
                break
            elif 'KernelWorkerStatus.ERROR' in current or 'KernelWorkerStatus.CANCELLED' in current:
                raise RuntimeError(f'Kaggle job failed for seed {seed}')
            time.sleep(60)
    summarize(sorted({101, *args.seeds}))


if __name__ == '__main__':
    main()
