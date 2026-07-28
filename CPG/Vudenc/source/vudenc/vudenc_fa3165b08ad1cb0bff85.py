def associate_cwes(self):...
"""docstring"""
cwe_map = []
if CVE.cve_cwe_map is not None:
cwe_map = [item[1] for item in CVE.cve_cwe_map if self.get_val('cve.id') ==
    item[0]]
return cwe_map
