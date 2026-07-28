# Fidelity audit

The main results must be described as faithful architectural adaptations under
a shared Python benchmark, not as exact replications of the papers' reported
experiments.

| Item | QDENN |
|---|---|
| Quantum recurrence | Source-paper circuit |
| Classical GRU/GRUCell | None |
| Measurement | First two Pauli-Z expectations |
| Qubits | `ceil(log2(vocabulary size))` |
| Vocabulary | 128, benchmark adaptation |
| Maximum length | 100, benchmark adaptation |
| Quantum layers | Per-token QDENN ansatz |
| Trainable quantum parameters | Depends on sequence length |
| Epochs | 10 |
| Batch size | 32 |
| Optimizer | SGD, momentum 0.9, weight decay 0.0001 |
| Learning rate | 0.01, not reported by paper |
| Original protocol | SARD code gadgets, 80/20 |
| This benchmark | Python source, fixed stratified 70/15/15 split seed 101 |

The QDENN paper does not report its learning rate. The value 0.01 is therefore
a declared reproduction choice and must not be attributed to the authors.

PennyLane broadcasting is an execution optimization. For each sample it applies
the same gates, in the same order, with the same parameters and measurements.
It does not change model capacity or the optimization objective.

## Permitted result claim

> We evaluate a faithful architectural adaptation of QDENN under a fixed-split
> Python vulnerability benchmark.

Do not claim exact reproduction of the original reported scores, superiority
under equal quantum resources, or quantum advantage.
