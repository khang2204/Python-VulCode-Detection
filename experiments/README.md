# Isolated experiments

This directory is intentionally separate from the production PAG-Vul pipeline.
Scripts, derived data, checkpoints, and reports created here must not overwrite
`artifacts/`, `CPG/`, `kaggle_deploy/`, or the canonical final results.

- `robustness/`: inference on semantics-preserving source transformations.
- `generalization/`: cross-benchmark train/test protocols.

Each scenario has its own `scripts/`, `artifacts/`, and `results/` folders.

## Current finalized PAG-Vul run

The current fixed-split experiment is in
`full_experiment_fixedsplit101_q10d5_lr002_20260727-005616/`. It uses split
seed 101 and training seeds 101, 202, and 303. The complete four-scenario
tables and artifact paths are documented in [`../RESULTS.md`](../RESULTS.md).
