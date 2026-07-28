# QDENN_SOTA in-domain results

Mean ± sample standard deviation over training seeds 101, 202, and 303 with
fixed split seed 101.

| Dataset | Accuracy | Balanced Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|
| BenchmarkPython | 0.5946 ± 0.0329 | 0.5224 ± 0.0168 | 0.4231 ± 0.0418 | 0.2500 ± 0.0674 | 0.3082 ± 0.0482 |
| VUDENC | 0.8332 ± 0.0011 | 0.5613 ± 0.0052 | 0.6331 ± 0.0194 | 0.1401 ± 0.0126 | 0.2292 ± 0.0161 |
| RealVuln-Human | 0.8281 ± 0.0413 | 0.5179 ± 0.0279 | 0.8486 ± 0.0074 | 0.9691 ± 0.0535 | 0.9044 ± 0.0258 |

These metrics were recovered by post-hoc inference from the nine completed
QDENN checkpoints on the fixed split-seed-101 test sets. No retraining was
performed.
