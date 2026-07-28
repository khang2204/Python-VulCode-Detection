"""
Module contains functions and CVE class for returning data from DB
"""
"""
    Class to hold CVE attributes
    """
cve_cwe_map = None
def __init__(self, cve_entry, column_names):...
for col_name in column_names:
setattr(self, col_name, cve_entry[column_names.index(col_name)])
self.cwe = self.associate_cwes()
def associate_cwes(self):...
"""docstring"""
cwe_map = []
if CVE.cve_cwe_map is not None:
cwe_map = [item[1] for item in CVE.cve_cwe_map if self.get_val('cve.id') ==
    item[0]]
return cwe_map
