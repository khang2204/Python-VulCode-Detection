# RealVuln — benchmark EDA

## Dataset overview

Each sample is a Python finding-context extracted from a human-authored repository. Vulnerable records retain the benchmark finding metadata and CWE; benign records are labelled context samples.

- Original labelled samples: **466**
- Successfully exported as CPG/graph: **431**
- Benign CPG samples: **69**
- Vulnerable CPG samples: **362**
- Vulnerable CWE categories: **58**

## Source-code metrics

Metrics are computed from the available source records. Block depth is the maximum nesting depth of Python control/definition blocks; branches count `if`/conditional expressions/exception handlers.

| Label | Samples | Parse OK | LOC mean / median | Depth mean / median | Branches mean / median | Loops mean / median | Try mean / median | Functions mean / median |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Benign | 78 | 33 | 19.6 / 21.0 | 0.94 / 0.0 | 0.51 / 0.0 | 0.04 / 0.0 | 0.05 / 0.0 | 0.59 / 0.0 |
| Vulnerable | 388 | 152 | 21.67 / 21.0 | 0.72 / 0.0 | 0.49 / 0.0 | 0.04 / 0.0 | 0.07 / 0.0 | 0.73 / 0.0 |

## Label quality check

Ten benign and ten vulnerable samples were selected uniformly at random using seed `20260725`. The selected source paths and labels are stored in `audit_samples.jsonl`; manual review notes are added below.

### Audit result

- Benign judged correct: **7/10**.
- Vulnerable judged correct: **10/10**.

### Benign audit samples

| Sample | Label/CWE | Source path | Manual review |
| --- | --- | --- | --- |
| 62d415cc2d972a1649e14f4820e5384ebf5fa89d82c41d52dc5cc71aa4cfbbad | CWE-1336 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_62d415cc2d972a1649e1.py` | The context itself concatenates username into a Jinja template; this contradicts its benign label. |
| 2988983940404d4b6f0fc7d809ccf157d16db7fef02a4e575fbc949ee633b190 | CWE-79 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_2988983940404d4b6f0f.py` | Shows SQL interpolation, insecure cookie use, and reflected output; benign label is contradicted. |
| 04775ed8ccc24e44ae632af56453845c1d367c8da26e9f904c64084959c77b66 | CWE-22 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_04775ed8ccc24e44ae63.py` | Allowlists path components and trigger names before resolution; benign label is supported. |
| e3790ff939ac611ed74efefedf27165350351c50797c8ca5f791e427a99d10e5 | CWE-89 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_e3790ff939ac611ed74e.py` | Uses a parameterized SQLite query; benign CWE-89 context is supported. |
| 769808a14cf6a0183624937dccaf099b6659d9549657eebd8b4030c00777850f | CWE-78 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_769808a14cf6a0183624.py` | Uses subprocess argument-list form, not a shell command string; benign label is supported. |
| b9c5a21d8205b1cba94f982dd83ecfcb284579a26c3f49df2c7ef71a87fa1b26 | CWE-1333 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_b9c5a21d8205b1cba94f.py` | Validates an email with a bounded regex; no catastrophic backtracking is visible. |
| 60f8f387732cf667082984e408bccc62714a272afa2c461634688aedbeb738dd | CWE-918 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_60f8f387732cf6670829.py` | The shown helper makes a fixed trusted request after constructing a connection; SSRF is not visible. |
| 30953f7856046ef8324f2f73a06434c3689d83512a7e0b72f755993231bc1c6d | CWE-918 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_30953f7856046ef8324f.py` | Contains unsafe pickle loading and SQL concatenation; benign label is contradicted. |
| 27079c3956aef4c564d4d9d886ad04dad18657517d85a87806af8de0fe2b1864 | CWE-79 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_27079c3956aef4c564d4.py` | Returns an empty string and has no reflected output; benign label is supported. |
| 0f014dc6dc36a8381033ea59b72eeb625c1345a508e1f2542937319c02e46c14 | CWE-798 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_0f014dc6dc36a8381033.py` | Static fixture data include a token-like value but no credential use or exposure is shown. |

### Vulnerable audit samples

| Sample | Label/CWE | Source path | Manual review |
| --- | --- | --- | --- |
| 621f9e6295e21ec0aa6364a18b5df5cc1c139b32480b975082d70179f6a8bb2e | CWE-22 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_621f9e6295e21ec0aa63.py` | User input reaches open/execfile without path restriction; CWE-22 is observable. |
| 14506ff78c5baab58c5484274e3d2f437a50538c860b07e1115c358620ac7eca | CWE-328 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_14506ff78c5baab58c54.py` | Prepends a secret to SHA-256 rather than using HMAC; CWE-328 is supported. |
| e844bb0cc9ba99bbaefee65e324fec2f5aee2a7791b003d687df7aa6830ab171 | CWE-1004 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_e844bb0cc9ba99bbaefe.py` | Sets a broadly permissive CSP and disables XSS protection; CWE-1004 is supported. |
| bd58fd0ef1b2d89cc31e8cf27dcd517d5c504a84899d820402fdedb3307a6d35 | CWE-89 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_bd58fd0ef1b2d89cc31e.py` | Builds SQL INSERT statements with percent interpolation; CWE-89 is supported. |
| 3abd9e969f57b13e083b9044175542b4b625ab36a97904f2efef5ee2125c26aa | CWE-16 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_3abd9e969f57b13e083b.py` | Command allowlist has a malformed tuple and weak character stripping; insecure configuration/control is supported. |
| be9a5064c38bc830579701384779472216baea57c40f51fe11329c627ea205ff | CWE-502 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_be9a5064c38bc8305797.py` | Loads request YAML with yaml.Loader; unsafe deserialization (CWE-502) is observable. |
| 9e1e32c84cfb6e760ca899967b27a9d628b4578d224f484c551bead42b666bde | CWE-798 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_9e1e32c84cfb6e760ca8.py` | Hard-coded user passwords are present in initialization data; CWE-798 is supported. |
| 43ae850b272732583d16c1cc14954647bb624abc288bd03c5ff52a6c5e64436e | CWE-611 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_43ae850b272732583d16.py` | Parses untrusted XML with lxml/DOM/SAX defaults; CWE-611 is supported. |
| 7d3484853a67902053fdf82c68f8f6602be219cedded987d27b54d774c64652f | CWE-22 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_7d3484853a67902053fd.py` | Joins an untrusted filename to a base path without canonical containment enforcement; CWE-22 is supported. |
| 14fdd8acffcfcddffedf18b83171b2eee9d7393506041ff1e36d096339e6790f | CWE-89 | `CPG/RealVulnHuman/source/realvuln_human/realvuln_human_14fdd8acffcfcddffedf.py` | Interpolates username into a SQL query in the vuln branch; CWE-89 is observable. |
