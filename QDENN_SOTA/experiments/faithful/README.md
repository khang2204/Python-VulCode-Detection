# Faithful QDENN in-domain adaptation

This directory contains an auditable implementation of QDENN, Scientific
Reports 12, 8053 (2022).

## Fidelity boundary

The quantum architecture, measurements, optimizer family, batch size, and
epoch count follow the source paper. QDENN follows the paper's
`ceil(log2(vocabulary size))` qubit rule; its 128-token Python benchmark
vocabulary therefore produces seven qubits.

The original papers operate on C/C++ code gadgets. The current benchmarks
contain Python samples, so this adaptation tokenizes each raw Python sample and
uses a train-only 128-token vocabulary. The benchmark protocol intentionally
uses one stratified 70/15/15 split with `split_seed=101`, while training
randomness changes across seeds 101, 202, and 303. These are declared benchmark
adaptations and must not be described as exact reproduction of the original
dataset protocol.

PennyLane input broadcasting is used to evaluate independent samples together.
It does not alter the circuit applied to any sample.

## Local/Colab command

Install PyTorch and PennyLane, then run one resumable unit:

```bash
python QDENN_SOTA/experiments/faithful/run_in_domain.py \
  --model qdenn \
  --dataset benchmarkpython \
  --seed 101 \
  --output /path/to/persistent/results
```

Use persistent storage for both `--output` and `--cache`. A checkpoint is
written after every epoch. Re-running the same command resumes an interrupted
run and skips a completed report.

For Google Colab, open `colab_in_domain.ipynb` and change only `REPO_ROOT` and
`DATASET`. One notebook executes all three training seeds for one dataset. The
accelerator should remain CPU because the audited PennyLane circuit uses
`default.qubit`.
