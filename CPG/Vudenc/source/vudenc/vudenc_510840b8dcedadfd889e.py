def __init__(self, cve_entry, column_names):...
for col_name in column_names:
setattr(self, col_name, cve_entry[column_names.index(col_name)])
self.cwe = self.associate_cwes()
