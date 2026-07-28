# Fixed-split PAG-Vul experiment

This directory contains the finalized experiment run used by the repository's
current results. Every in-domain dataset uses the same fixed stratified split
(split seed 101); the reported mean and sample standard deviation use training
seeds 101, 202, and 303.

Configuration: 10-qubit, depth-5 quantum circuit; attention/value dimension
64; learning rate 0.002 for both Classical and Quantum heads; 50 warm-up and
50 head-training epochs.

The complete In-domain, In-domain 10%, Generalization, and Long-tail CWE
tables are maintained in [`../../RESULTS.md`](../../RESULTS.md). Raw results
remain below this directory and are not overwritten by aggregation:

- `in_domain/runs/`
- `in_domain_ten_percent/`
- `generalization/output/generalization_results/`
- `long_tail_cwe_recall/`
