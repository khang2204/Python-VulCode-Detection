#!/usr/bin/env python3
"""Rebuild dataset-level EDA and deterministic audit samples for PAG-Vul benchmarks."""
from __future__ import annotations

import ast
import csv
import json
import random
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "EDA"

# Notes are part of the deterministic audit, rather than prose that is lost the
# next time this script regenerates a README.  They record only what is visible
# in the exported source context (not a claim about omitted surrounding code).
AUDIT_NOTES = {
    "BenchmarkTest01136": "Safe guard/value handling is present; no dangerous data flow is visible.",
    "BenchmarkTest00423": "The source uses the safe variant for its tested operation; benign label is supported.",
    "BenchmarkTest01036": "Input is constrained before the relevant operation; no vulnerable sink is reached.",
    "BenchmarkTest00216": "The tested path uses a safe constant or validated value; benign label is supported.",
    "BenchmarkTest00013": "The code follows the benchmark's safe implementation path; no exploit primitive is visible.",
    "BenchmarkTest00936": "Safe handling is used in the tested flow; no insecure behavior is visible.",
    "BenchmarkTest00491": "The source contains the safe counterpart of the benchmark pattern; benign label is supported.",
    "BenchmarkTest00798": "Guarded handling prevents the dangerous operation in this test case.",
    "BenchmarkTest00408": "The relevant value is handled safely; no vulnerable data flow is visible.",
    "BenchmarkTest00275": "The sample implements the non-vulnerable benchmark variant.",
    "BenchmarkTest00180": "User-controlled path reaches file access without a containment check; CWE-22 is observable.",
    "BenchmarkTest00096": "Untrusted value reaches HTML output without escaping; CWE-79 is observable.",
    "BenchmarkTest00431": "Untrusted data reaches command execution; CWE-78 is observable.",
    "BenchmarkTest00097": "The response reflects unescaped input into HTML; CWE-79 is observable.",
    "BenchmarkTest00874": "The source uses a weak hash for a security-sensitive purpose; CWE-328 is supported.",
    "BenchmarkTest00713": "A weak hash is used where a stronger construction is required; CWE-328 is supported.",
    "BenchmarkTest00268": "The command construction/execution path accepts unsafe input; CWE-78 is observable.",
    "BenchmarkTest00718": "Cookie/security attributes are missing in the shown response path; CWE-614 is supported.",
    "BenchmarkTest00605": "Untrusted serialized input is deserialized with an unsafe primitive; CWE-502 is observable.",
    "BenchmarkTest00304": "User data is interpolated into an XPath expression; CWE-643 is observable.",
    "vudenc_8e724188840790e600ac": "Generates a Fernet key; no vulnerability is visible in this short context.",
    "vudenc_9bd3852c91e04d837f70": "Checks server liveness before posting; no dangerous flow is visible.",
    "vudenc_323e55b556f59cd1313a": "Formats a field through framework helpers; no vulnerability is visible.",
    "vudenc_ce4f87b8e7138a6005ea": "Writes generated tree entries, but this context exposes no attacker-controlled path.",
    "vudenc_f68c98b5350f81dd220f": "Performs matrix arithmetic only; benign label is consistent with visible code.",
    "vudenc_4fff20b7cba88e8a2cb9": "Delegates a command to process_vote; no insecure operation is shown here.",
    "vudenc_599e36bf94e2c439da45": "Conditionally dispatches a signal; no vulnerability is visible.",
    "vudenc_c4de1a668cbab7047bc5": "Queue-processing loop is visible, with no security-sensitive sink in context.",
    "vudenc_538fe44fb215fcf4bb9c": "Builds storage configuration from volume fields; no exploit primitive is visible here.",
    "vudenc_a670556e988ff72dcbab": "Recursively normalizes XML attributes; no vulnerability is visible.",
    "vudenc_c95fb3d231bd8498ba52": "Incorrect vulnerable label: lexer token construction has no XSS or other dangerous sink.",
    "vudenc_b45886f59eb9845dd0e7": "Correct vulnerable label: get_files output is returned by the API; the fixing diff removed submit.tmp_path from that output, confirming path disclosure.",
    "vudenc_be2dc1d266d8925cef37": "Incorrect vulnerable label: the framework safe_eval use alone is not a demonstrated exploit path.",
    "vudenc_650dd360738f4e8f4288": "Incorrect vulnerable label: model-field declarations contain no vulnerable operation.",
    "vudenc_1fa8d91114b2295b5013": "Correct vulnerable label: Jinja Environment is created without autoescape, so attacker-controlled template values can produce XSS.",
    "vudenc_abaff25460b572fd597d": "Correct vulnerable label: postid is interpolated into SQL with percent formatting, exposing SQL injection.",
    "vudenc_f9a50064c36b571e3ae9": "Correct vulnerable label: the old Bot setup uses the removed XSRF-client configuration; its fixing commit replaces this cookie/XSRF flow with token authentication.",
    "vudenc_9be66e72955fa1b25799": "Correct vulnerable label: request-controlled next is passed directly to redirect, creating an open redirect.",
    "vudenc_bf32a149411fd0956e00": "Incorrect vulnerable label: a timing loop has no vulnerability-relevant sink.",
    "vudenc_59a77e81d1ced30aafe5": "Correct vulnerable label: this POST test relies on browser-session authentication; the fixing diff requires an authorization token to prevent XSRF.",
    "62d415cc2d972a1649e14f4820e5384ebf5fa89d82c41d52dc5cc71aa4cfbbad": "The context itself concatenates username into a Jinja template; this contradicts its benign label.",
    "2988983940404d4b6f0fc7d809ccf157d16db7fef02a4e575fbc949ee633b190": "Shows SQL interpolation, insecure cookie use, and reflected output; benign label is contradicted.",
    "04775ed8ccc24e44ae632af56453845c1d367c8da26e9f904c64084959c77b66": "Allowlists path components and trigger names before resolution; benign label is supported.",
    "e3790ff939ac611ed74efefedf27165350351c50797c8ca5f791e427a99d10e5": "Uses a parameterized SQLite query; benign CWE-89 context is supported.",
    "769808a14cf6a0183624937dccaf099b6659d9549657eebd8b4030c00777850f": "Uses subprocess argument-list form, not a shell command string; benign label is supported.",
    "b9c5a21d8205b1cba94f982dd83ecfcb284579a26c3f49df2c7ef71a87fa1b26": "Validates an email with a bounded regex; no catastrophic backtracking is visible.",
    "60f8f387732cf667082984e408bccc62714a272afa2c461634688aedbeb738dd": "The shown helper makes a fixed trusted request after constructing a connection; SSRF is not visible.",
    "30953f7856046ef8324f2f73a06434c3689d83512a7e0b72f755993231bc1c6d": "Contains unsafe pickle loading and SQL concatenation; benign label is contradicted.",
    "27079c3956aef4c564d4d9d886ad04dad18657517d85a87806af8de0fe2b1864": "Returns an empty string and has no reflected output; benign label is supported.",
    "0f014dc6dc36a8381033ea59b72eeb625c1345a508e1f2542937319c02e46c14": "Static fixture data include a token-like value but no credential use or exposure is shown.",
    "621f9e6295e21ec0aa6364a18b5df5cc1c139b32480b975082d70179f6a8bb2e": "User input reaches open/execfile without path restriction; CWE-22 is observable.",
    "14506ff78c5baab58c5484274e3d2f437a50538c860b07e1115c358620ac7eca": "Prepends a secret to SHA-256 rather than using HMAC; CWE-328 is supported.",
    "e844bb0cc9ba99bbaefee65e324fec2f5aee2a7791b003d687df7aa6830ab171": "Sets a broadly permissive CSP and disables XSS protection; CWE-1004 is supported.",
    "bd58fd0ef1b2d89cc31e8cf27dcd517d5c504a84899d820402fdedb3307a6d35": "Builds SQL INSERT statements with percent interpolation; CWE-89 is supported.",
    "3abd9e969f57b13e083b9044175542b4b625ab36a97904f2efef5ee2125c26aa": "Command allowlist has a malformed tuple and weak character stripping; insecure configuration/control is supported.",
    "be9a5064c38bc830579701384779472216baea57c40f51fe11329c627ea205ff": "Loads request YAML with yaml.Loader; unsafe deserialization (CWE-502) is observable.",
    "9e1e32c84cfb6e760ca899967b27a9d628b4578d224f484c551bead42b666bde": "Hard-coded user passwords are present in initialization data; CWE-798 is supported.",
    "43ae850b272732583d16c1cc14954647bb624abc288bd03c5ff52a6c5e64436e": "Parses untrusted XML with lxml/DOM/SAX defaults; CWE-611 is supported.",
    "7d3484853a67902053fdf82c68f8f6602be219cedded987d27b54d774c64652f": "Joins an untrusted filename to a base path without canonical containment enforcement; CWE-22 is supported.",
    "14fdd8acffcfcddffedf18b83171b2eee9d7393506041ff1e36d096339e6790f": "Interpolates username into a SQL query in the vuln branch; CWE-89 is observable.",
}

AUDIT_SUMMARIES = {
    "BenchmarkPython": [
        "Benign judged correct: **10/10**.",
        "Vulnerable judged correct: **10/10**.",
    ],
    "VUDENC": [
        "Benign judged correct: **10/10**.",
        "Vulnerable judged correct: **6/10**.",
    ],
    "RealVuln": [
        "Benign judged correct: **7/10**.",
        "Vulnerable judged correct: **10/10**.",
    ],
}


def metric(source: str) -> dict[str, int | bool]:
    out = {"loc": len(source.splitlines()), "depth": 0, "branches": 0, "loops": 0, "tries": 0, "functions": 0, "parse_ok": True}
    try:
        tree = ast.parse(source)
    except SyntaxError:
        out["parse_ok"] = False
        return out
    blocks = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.With, ast.AsyncWith)
    def walk(node: ast.AST, depth: int) -> None:
        current = depth + int(isinstance(node, blocks))
        out["depth"] = max(out["depth"], current)
        for child in ast.iter_child_nodes(node): walk(child, current)
    walk(tree, 0)
    nodes = list(ast.walk(tree))
    out["branches"] = sum(isinstance(n, (ast.If, ast.IfExp, ast.ExceptHandler)) for n in nodes)
    out["loops"] = sum(isinstance(n, (ast.For, ast.AsyncFor, ast.While)) for n in nodes)
    out["tries"] = sum(isinstance(n, ast.Try) for n in nodes)
    out["functions"] = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in nodes)
    return out


def summarize(rows: list[dict]) -> dict:
    result = {}
    for label, name in ((0, "Benign"), (1, "Vulnerable")):
        group = [r for r in rows if r["label"] == label]
        result[name] = {"samples": len(group), "parse_ok": sum(r["metrics"]["parse_ok"] for r in group)}
        for key in ("loc", "depth", "branches", "loops", "tries", "functions"):
            values = [r["metrics"][key] for r in group]
            result[name][key] = {"mean": round(statistics.fmean(values), 2), "median": round(statistics.median(values), 2)}
    return result


def benchmarkpython() -> tuple[str, str, list[dict], int, int, dict]:
    rows=[]
    with (ROOT / "data/BenchmarkPython/expectedresults-0.1.csv").open() as f:
        for line in f:
            if line.startswith("#") or not line.strip(): continue
            name, category, vulnerable, cwe = [x.strip() for x in next(csv.reader([line]))]
            path=ROOT / "data/BenchmarkPython/testcode" / f"{name}.py"
            source=path.read_text(errors="replace")
            # Source text is needed only while calculating the metric.  Keeping
            # every file here makes the VUDENC pass needlessly memory-heavy.
            rows.append({"id":name,"label":int(vulnerable=="true"),"cwe":f"CWE-{cwe}" if vulnerable=="true" else "BENIGN","path":path,"metrics":metric(source)})
    report=json.loads((ROOT/"artifacts/benchmarkpython_binary_pyg/report.json").read_text())
    return "BenchmarkPython", "Each sample is one OWASP BenchmarkPython test-case Python file, paired with its expected-result record (binary vulnerability label and CWE for vulnerable cases).", rows, len(rows), report["exported_graphs"], report


def metadata_dataset(name: str, meta: Path, source_root: Path, report_path: Path, description: str) -> tuple[str,str,list[dict],int,int,dict]:
    rows=[]
    for line in meta.read_text().splitlines():
        item=json.loads(line); path=source_root / item["sample_file"]
        if not path.is_file(): continue
        source=path.read_text(errors="replace")
        vulnerable=str(item.get("real_vulnerability", "")).lower()=="true" or int(item.get("label",0))==1
        rows.append({"id":item.get("pair_id",item["sample_file"]),"label":int(vulnerable),"cwe":item.get("primary_cwe") or item.get("cwe") or "UNKNOWN","path":path,"metrics":metric(source),"evidence":item.get("evidence_description","")})
    report=json.loads(report_path.read_text())
    return name, description, rows, report.get("raw_labelled_samples", report.get("prepared_contexts", len(rows))), report["exported_graphs"], report


def write(name: str, description: str, rows: list[dict], raw: int, exported: int, report: dict) -> None:
    folder=OUT/name; folder.mkdir(parents=True, exist_ok=True)
    stats=summarize(rows); counts=report["binary_counts"]; cwes=report.get("vulnerable_counts_by_cwe",{})
    rnd=random.Random(20260725); audit=[]
    for label in (0,1): audit += rnd.sample([r for r in rows if r["label"]==label], 10)
    missing = [r["id"] for r in audit if r["id"] not in AUDIT_NOTES]
    if missing:
        raise RuntimeError(f"Missing manual audit notes for: {', '.join(missing)}")
    audit_records = [
        {**{k: (str(v) if k == "path" else v) for k, v in r.items() if k not in {"source", "metrics"}},
         "manual_review": AUDIT_NOTES[r["id"]]} for r in audit
    ]
    (folder/"audit_samples.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in audit_records), encoding="utf-8")
    lines=[f"# {name} — benchmark EDA", "", "## Dataset overview", "", description, "", f"- Original labelled samples: **{raw:,}**", f"- Successfully exported as CPG/graph: **{exported:,}**", f"- Benign CPG samples: **{counts['benign']:,}**", f"- Vulnerable CPG samples: **{counts['vulnerable']:,}**", f"- Vulnerable CWE categories: **{len(cwes):,}**", "", "## Source-code metrics", "", "Metrics are computed from the available source records. Block depth is the maximum nesting depth of Python control/definition blocks; branches count `if`/conditional expressions/exception handlers.", "", "| Label | Samples | Parse OK | LOC mean / median | Depth mean / median | Branches mean / median | Loops mean / median | Try mean / median | Functions mean / median |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for label in ("Benign","Vulnerable"):
        s=stats[label]; lines.append(f"| {label} | {s['samples']:,} | {s['parse_ok']:,} | {s['loc']['mean']} / {s['loc']['median']} | {s['depth']['mean']} / {s['depth']['median']} | {s['branches']['mean']} / {s['branches']['median']} | {s['loops']['mean']} / {s['loops']['median']} | {s['tries']['mean']} / {s['tries']['median']} | {s['functions']['mean']} / {s['functions']['median']} |")
    lines += ["", "## Label quality check", "", "Ten benign and ten vulnerable samples were selected uniformly at random using seed `20260725`. The selected source paths and labels are stored in `audit_samples.jsonl`; manual review notes are added below.", "", "### Audit result", ""]
    lines += [f"- {result}" for result in AUDIT_SUMMARIES[name]]
    lines.append("")
    for label, title in ((0,"Benign"),(1,"Vulnerable")):
        lines += [f"### {title} audit samples", "", "| Sample | Label/CWE | Source path | Manual review |", "| --- | --- | --- | --- |"]
        for r in [x for x in audit if x['label']==label]:
            note = AUDIT_NOTES[r["id"]].replace("|", "\\|")
            lines.append(f"| {r['id']} | {r['cwe']} | `{r['path'].relative_to(ROOT)}` | {note} |")
        lines.append("")
    (folder/f"EDA_{name}.md").write_text("\n".join(lines),encoding="utf-8")
    (folder/"metrics.json").write_text(json.dumps({"summary":stats,"raw_labelled_samples":raw,"exported_graphs":exported,"binary_counts":counts,"vulnerable_cwe_counts":cwes},indent=2),encoding="utf-8")


def main() -> None:
    targets=set(sys.argv[1:] or ("benchmarkpython","vudenc","realvuln"))
    if "benchmarkpython" in targets: write(*benchmarkpython())
    if "vudenc" in targets: write(*metadata_dataset("VUDENC", ROOT/"CPG/Vudenc/metadata.jsonl", ROOT/"CPG/Vudenc/source", ROOT/"artifacts/vudenc_binary_pyg/report.json", "Each sample is a labelled Python code block/context from the VUDENC corpus; the exported record carries a binary label and VUDENC vulnerability type for vulnerable samples."))
    if "realvuln" in targets: write(*metadata_dataset("RealVuln", ROOT/"CPG/RealVulnHuman/metadata.jsonl", ROOT/"CPG/RealVulnHuman/source", ROOT/"artifacts/realvuln_human_binary_pyg/report.json", "Each sample is a Python finding-context extracted from a human-authored repository. Vulnerable records retain the benchmark finding metadata and CWE; benign records are labelled context samples."))

if __name__ == "__main__": main()
