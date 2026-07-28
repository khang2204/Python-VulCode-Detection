# HQCDNN Long-tail CWE results

Mean ± sample standard deviation over training seeds 101, 202, and 303 with
fixed split seed 101.

| Qubits | Dataset | Rare samples | Rare-CWE Recall | Common samples | Common-CWE Recall |
|---:|---|---:|---:|---:|---:|
| 2 | BenchmarkPython | 20 | 0.3333 ± 0.2887 | 48 | 0.3542 ± 0.3111 |
| 2 | VUDENC | 131 | 0.4453 ± 0.0447 | 290 | 0.5023 ± 0.0190 |
| 2 | RealVuln-Human | 9 | 1.0000 ± 0.0000 | 45 | 1.0000 ± 0.0000 |
| 4 | BenchmarkPython | 20 | 0.5000 ± 0.0500 | 48 | 0.5694 ± 0.0434 |
| 4 | VUDENC | 131 | 0.4758 ± 0.0384 | 290 | 0.5425 ± 0.0535 |
| 4 | RealVuln-Human | 9 | 1.0000 ± 0.0000 | 45 | 0.9926 ± 0.0128 |

Common-CWE samples are vulnerable test samples whose CWE is not in the rare
CWE set derived exclusively from the fixed training split.
