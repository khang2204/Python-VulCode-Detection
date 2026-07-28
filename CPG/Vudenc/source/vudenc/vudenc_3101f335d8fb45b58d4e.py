def process_list(self, data):...
"""docstring"""
cves_to_process = data['cve_list']
cves_to_process = filter(None, cves_to_process)
answer = {}
if not cves_to_process:
return answer
column_names = ['cve.id', 'redhat_url', 'secondary_url', 'cve.name',
    'severity.name', 'published_date', 'modified_date', 'iava', 'description']
cve_query = 'SELECT %s from cve' % ', '.join(column for column in column_names)
cve_query = cve_query + ' LEFT JOIN severity ON severity_id = severity.id'
cve_query = cve_query + ' WHERE cve.name IN %s'
self.cursor.execute(cve_query, [tuple(cves_to_process)])
cves = self.cursor.fetchall()
cwe_map = self.get_cve_cwe_map([cve[column_names.index('cve.id')] for cve in
    cves])
CVE.cve_cwe_map = cwe_map
cve_list = []
for cve_entry in cves:
cve = CVE(cve_entry, column_names)
return self.construct_answer(cve_list)
cve_list.append(cve)
