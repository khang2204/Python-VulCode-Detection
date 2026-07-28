# Cross-benchmark generalization

| Train → Test | Method | Accuracy | Bal. Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| benchmarkpython → realvuln_human | Classical | 47.33% ± 8.47% | 50.07% ± 3.16% | 84.09% ± 1.74% | 46.04% ± 12.28% | 58.82% ± 10.63% |
| benchmarkpython → realvuln_human | Quantum | 51.35% ± 7.73% | 50.32% ± 6.18% | 83.89% ± 3.36% | 51.84% ± 8.62% | 63.90% ± 7.69% |
| benchmarkpython → vudenc | Classical | 35.78% ± 5.92% | 40.87% ± 3.15% | 13.60% ± 1.14% | 48.75% ± 3.42% | 21.23% ± 1.41% |
| benchmarkpython → vudenc | Quantum | 31.22% ± 6.54% | 41.60% ± 3.09% | 14.32% ± 1.06% | 57.68% ± 6.44% | 22.91% ± 1.54% |
| realvuln_human → benchmarkpython | Classical | 36.78% ± 0.05% | 50.02% ± 0.04% | 36.76% ± 0.02% | 100.00% ± 0.00% | 53.76% ± 0.02% |
| realvuln_human → benchmarkpython | Quantum | 36.75% ± 0.00% | 50.00% ± 0.00% | 36.75% ± 0.00% | 100.00% ± 0.00% | 53.75% ± 0.00% |
| realvuln_human → vudenc | Classical | 32.39% ± 4.76% | 52.03% ± 2.60% | 18.50% ± 1.04% | 82.42% ± 2.60% | 30.20% ± 1.36% |
| realvuln_human → vudenc | Quantum | 29.02% ± 3.16% | 51.86% ± 0.99% | 18.36% ± 0.37% | 87.23% ± 2.96% | 30.33% ± 0.42% |
| vudenc → benchmarkpython | Classical | 39.57% ± 2.05% | 48.83% ± 1.47% | 36.09% ± 0.78% | 83.78% ± 8.10% | 50.40% ± 2.04% |
| vudenc → benchmarkpython | Quantum | 39.32% ± 2.72% | 47.93% ± 1.62% | 35.60% ± 0.84% | 80.38% ± 6.11% | 49.30% ± 1.42% |
| vudenc → realvuln_human | Classical | 42.85% ± 3.71% | 46.62% ± 1.45% | 81.76% ± 1.11% | 41.07% ± 4.83% | 54.58% ± 4.54% |
| vudenc → realvuln_human | Quantum | 44.55% ± 2.58% | 46.07% ± 4.84% | 81.66% ± 2.92% | 43.83% ± 1.84% | 57.03% ± 2.13% |
