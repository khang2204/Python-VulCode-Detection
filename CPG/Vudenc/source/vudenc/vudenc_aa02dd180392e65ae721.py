def get_cve_names_for_erratum_id(self, id):...
"""docstring"""
cve_query = 'SELECT name FROM cve'
cve_query += ' JOIN errata_cve ON cve_id = cve.id'
cve_query += ' WHERE errata_cve.errata_id = %s' % str(id)
self.cursor.execute(cve_query)
cve_names = self.cursor.fetchall()
cve_name_list = []
for cve_name in cve_names:
cve_name_list.append(cve_name[0])
return cve_name_list
