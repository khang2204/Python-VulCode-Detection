def process_list(self, data):...
"""docstring"""
errata_to_process = data['errata_list']
errata_to_process = filter(None, errata_to_process)
answer = {}
if not errata_to_process:
return answer
errata_query = (
    'SELECT errata.id, errata.name, synopsis, severity.name, description,')
errata_query += ' solution, issued, updated'
errata_query += ' FROM errata'
errata_query += ' LEFT JOIN severity ON severity_id = severity.id'
errata_query += ' WHERE errata.name IN %s'
self.cursor.execute(errata_query, [tuple(errata_to_process)])
errata = self.cursor.fetchall()
erratum_list = []
for id, name, synopsis, severity, description, solution, issued, updated in errata:
new_erratum = Errata(id, name, synopsis, severity, description, solution,
    issued, updated)
errata_dict = {}
new_erratum.set_cve_names(self.get_cve_names_for_erratum_id(id))
for e in erratum_list:
new_erratum.set_packages(self.get_package_list_for_erratum_id(id))
errata_dict[e.get_val('name')] = e.get_val('mydict')
answer['errata_list'] = errata_dict
erratum_list.append(new_erratum)
return answer
