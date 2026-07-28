# QDENN Long-tail CWE results

Mean ± sample standard deviation over training seeds 101, 202, and 303 with
fixed split seed 101.

| Dataset | Rare samples | Rare-CWE Recall | Common samples | Common-CWE Recall |
|---|---:|---:|---:|---:|
| BenchmarkPython | 20 | 0.3833 ± 0.0577 | 48 | 0.1944 ± 0.0789 |
| VUDENC | 131 | 0.1450 ± 0.0275 | 290 | 0.1379 ± 0.0150 |
| RealVuln-Human | 9 | 0.9630 ± 0.0642 | 45 | 0.9704 ± 0.0513 |

Common-CWE samples are vulnerable test samples whose CWE is not in the rare
CWE set derived exclusively from the fixed training split.
