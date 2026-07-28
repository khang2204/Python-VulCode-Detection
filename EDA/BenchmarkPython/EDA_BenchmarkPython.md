# BenchmarkPython — benchmark EDA

## Dataset overview

Each sample is one OWASP BenchmarkPython test-case Python file, paired with its expected-result record (binary vulnerability label and CWE for vulnerable cases).

- Original labelled samples: **1,230**
- Successfully exported as CPG/graph: **1,230**
- Benign CPG samples: **778**
- Vulnerable CPG samples: **452**
- Vulnerable CWE categories: **14**

## Source-code metrics

Metrics are computed from the available source records. Block depth is the maximum nesting depth of Python control/definition blocks; branches count `if`/conditional expressions/exception handlers.

| Label | Samples | Parse OK | LOC mean / median | Depth mean / median | Branches mean / median | Loops mean / median | Try mean / median | Functions mean / median |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Benign | 778 | 778 | 63.87 / 64.0 | 3.57 / 4.0 | 2.72 / 3.0 | 0.32 / 0.0 | 0.48 / 0.0 | 3.0 / 3.0 |
| Vulnerable | 452 | 452 | 62.98 / 64.0 | 3.56 / 4.0 | 2.76 / 3.0 | 0.29 / 0.0 | 0.42 / 0.0 | 3.0 / 3.0 |

## Label quality check

Ten benign and ten vulnerable samples were selected uniformly at random using seed `20260725`. The selected source paths and labels are stored in `audit_samples.jsonl`; manual review notes are added below.

### Audit result

- Benign judged correct: **10/10**.
- Vulnerable judged correct: **10/10**.

### Benign audit samples

| Sample | Label/CWE | Source path | Manual review |
| --- | --- | --- | --- |
| BenchmarkTest01136 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest01136.py` | Safe guard/value handling is present; no dangerous data flow is visible. |
| BenchmarkTest00423 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00423.py` | The source uses the safe variant for its tested operation; benign label is supported. |
| BenchmarkTest01036 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest01036.py` | Input is constrained before the relevant operation; no vulnerable sink is reached. |
| BenchmarkTest00216 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00216.py` | The tested path uses a safe constant or validated value; benign label is supported. |
| BenchmarkTest00013 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00013.py` | The code follows the benchmark's safe implementation path; no exploit primitive is visible. |
| BenchmarkTest00936 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00936.py` | Safe handling is used in the tested flow; no insecure behavior is visible. |
| BenchmarkTest00491 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00491.py` | The source contains the safe counterpart of the benchmark pattern; benign label is supported. |
| BenchmarkTest00798 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00798.py` | Guarded handling prevents the dangerous operation in this test case. |
| BenchmarkTest00408 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00408.py` | The relevant value is handled safely; no vulnerable data flow is visible. |
| BenchmarkTest00275 | BENIGN | `data/BenchmarkPython/testcode/BenchmarkTest00275.py` | The sample implements the non-vulnerable benchmark variant. |

### Vulnerable audit samples

| Sample | Label/CWE | Source path | Manual review |
| --- | --- | --- | --- |
| BenchmarkTest00180 | CWE-22 | `data/BenchmarkPython/testcode/BenchmarkTest00180.py` | User-controlled path reaches file access without a containment check; CWE-22 is observable. |
| BenchmarkTest00096 | CWE-79 | `data/BenchmarkPython/testcode/BenchmarkTest00096.py` | Untrusted value reaches HTML output without escaping; CWE-79 is observable. |
| BenchmarkTest00431 | CWE-78 | `data/BenchmarkPython/testcode/BenchmarkTest00431.py` | Untrusted data reaches command execution; CWE-78 is observable. |
| BenchmarkTest00097 | CWE-79 | `data/BenchmarkPython/testcode/BenchmarkTest00097.py` | The response reflects unescaped input into HTML; CWE-79 is observable. |
| BenchmarkTest00874 | CWE-328 | `data/BenchmarkPython/testcode/BenchmarkTest00874.py` | The source uses a weak hash for a security-sensitive purpose; CWE-328 is supported. |
| BenchmarkTest00713 | CWE-328 | `data/BenchmarkPython/testcode/BenchmarkTest00713.py` | A weak hash is used where a stronger construction is required; CWE-328 is supported. |
| BenchmarkTest00268 | CWE-78 | `data/BenchmarkPython/testcode/BenchmarkTest00268.py` | The command construction/execution path accepts unsafe input; CWE-78 is observable. |
| BenchmarkTest00718 | CWE-614 | `data/BenchmarkPython/testcode/BenchmarkTest00718.py` | Cookie/security attributes are missing in the shown response path; CWE-614 is supported. |
| BenchmarkTest00605 | CWE-502 | `data/BenchmarkPython/testcode/BenchmarkTest00605.py` | Untrusted serialized input is deserialized with an unsafe primitive; CWE-502 is observable. |
| BenchmarkTest00304 | CWE-643 | `data/BenchmarkPython/testcode/BenchmarkTest00304.py` | User data is interpolated into an XPath expression; CWE-643 is observable. |
