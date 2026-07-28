# VUDENC — benchmark EDA

## Dataset overview

Each sample is a labelled Python code block/context from the VUDENC corpus; the exported record carries a binary label and VUDENC vulnerability type for vulnerable samples.

- Original labelled samples: **15,841**
- Successfully exported as CPG/graph: **15,840**
- Benign CPG samples: **13,035**
- Vulnerable CPG samples: **2,805**
- Vulnerable CWE categories: **7**

## Source-code metrics

Metrics are computed from the available source records. Block depth is the maximum nesting depth of Python control/definition blocks; branches count `if`/conditional expressions/exception handlers.

| Label | Samples | Parse OK | LOC mean / median | Depth mean / median | Branches mean / median | Loops mean / median | Try mean / median | Functions mean / median |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Benign | 13,036 | 6,322 | 8.6 / 5.0 | 0.48 / 0.0 | 0.01 / 0.0 | 0.0 / 0.0 | 0.0 / 0.0 | 0.51 / 0.0 |
| Vulnerable | 2,805 | 1,041 | 25.63 / 14 | 0.35 / 0 | 0.01 / 0 | 0.0 / 0 | 0.0 / 0 | 0.41 / 0 |

## Label quality check

Ten benign and ten vulnerable samples were selected uniformly at random using seed `20260725`. The selected source paths and labels are stored in `audit_samples.jsonl`; manual review notes are added below.

### Audit result

- Benign judged correct: **10/10**.
- Vulnerable judged correct: **6/10**.

### Benign audit samples

| Sample | Label/CWE | Source path | Manual review |
| --- | --- | --- | --- |
| vudenc_8e724188840790e600ac | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_8e724188840790e600ac.py` | Generates a Fernet key; no vulnerability is visible in this short context. |
| vudenc_9bd3852c91e04d837f70 | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_9bd3852c91e04d837f70.py` | Checks server liveness before posting; no dangerous flow is visible. |
| vudenc_323e55b556f59cd1313a | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_323e55b556f59cd1313a.py` | Formats a field through framework helpers; no vulnerability is visible. |
| vudenc_ce4f87b8e7138a6005ea | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_ce4f87b8e7138a6005ea.py` | Writes generated tree entries, but this context exposes no attacker-controlled path. |
| vudenc_f68c98b5350f81dd220f | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_f68c98b5350f81dd220f.py` | Performs matrix arithmetic only; benign label is consistent with visible code. |
| vudenc_4fff20b7cba88e8a2cb9 | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_4fff20b7cba88e8a2cb9.py` | Delegates a command to process_vote; no insecure operation is shown here. |
| vudenc_599e36bf94e2c439da45 | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_599e36bf94e2c439da45.py` | Conditionally dispatches a signal; no vulnerability is visible. |
| vudenc_c4de1a668cbab7047bc5 | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_c4de1a668cbab7047bc5.py` | Queue-processing loop is visible, with no security-sensitive sink in context. |
| vudenc_538fe44fb215fcf4bb9c | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_538fe44fb215fcf4bb9c.py` | Builds storage configuration from volume fields; no exploit primitive is visible here. |
| vudenc_a670556e988ff72dcbab | BENIGN | `CPG/Vudenc/source/vudenc/vudenc_a670556e988ff72dcbab.py` | Recursively normalizes XML attributes; no vulnerability is visible. |

### Vulnerable audit samples

| Sample | Label/CWE | Source path | Manual review |
| --- | --- | --- | --- |
| vudenc_c95fb3d231bd8498ba52 | VUDENC-TYPE-2 | `CPG/Vudenc/source/vudenc/vudenc_c95fb3d231bd8498ba52.py` | Incorrect vulnerable label: lexer token construction has no XSS or other dangerous sink. |
| vudenc_b45886f59eb9845dd0e7 | VUDENC-TYPE-1 | `CPG/Vudenc/source/vudenc/vudenc_b45886f59eb9845dd0e7.py` | Correct vulnerable label: get_files output is returned by the API; the fixing diff removed submit.tmp_path from that output, confirming path disclosure. |
| vudenc_be2dc1d266d8925cef37 | VUDENC-TYPE-4 | `CPG/Vudenc/source/vudenc/vudenc_be2dc1d266d8925cef37.py` | Incorrect vulnerable label: the framework safe_eval use alone is not a demonstrated exploit path. |
| vudenc_650dd360738f4e8f4288 | VUDENC-TYPE-6 | `CPG/Vudenc/source/vudenc/vudenc_650dd360738f4e8f4288.py` | Incorrect vulnerable label: model-field declarations contain no vulnerable operation. |
| vudenc_1fa8d91114b2295b5013 | VUDENC-TYPE-3 | `CPG/Vudenc/source/vudenc/vudenc_1fa8d91114b2295b5013.py` | Correct vulnerable label: Jinja Environment is created without autoescape, so attacker-controlled template values can produce XSS. |
| vudenc_abaff25460b572fd597d | VUDENC-TYPE-4 | `CPG/Vudenc/source/vudenc/vudenc_abaff25460b572fd597d.py` | Correct vulnerable label: postid is interpolated into SQL with percent formatting, exposing SQL injection. |
| vudenc_f9a50064c36b571e3ae9 | VUDENC-TYPE-5 | `CPG/Vudenc/source/vudenc/vudenc_f9a50064c36b571e3ae9.py` | Correct vulnerable label: the old Bot setup uses the removed XSRF-client configuration; its fixing commit replaces this cookie/XSRF flow with token authentication. |
| vudenc_9be66e72955fa1b25799 | VUDENC-TYPE-5 | `CPG/Vudenc/source/vudenc/vudenc_9be66e72955fa1b25799.py` | Correct vulnerable label: request-controlled next is passed directly to redirect, creating an open redirect. |
| vudenc_bf32a149411fd0956e00 | VUDENC-TYPE-5 | `CPG/Vudenc/source/vudenc/vudenc_bf32a149411fd0956e00.py` | Incorrect vulnerable label: a timing loop has no vulnerability-relevant sink. |
| vudenc_59a77e81d1ced30aafe5 | VUDENC-TYPE-5 | `CPG/Vudenc/source/vudenc/vudenc_59a77e81d1ced30aafe5.py` | Correct vulnerable label: this POST test relies on browser-session authentication; the fixing diff requires an authorization token to prevent XSRF. |
