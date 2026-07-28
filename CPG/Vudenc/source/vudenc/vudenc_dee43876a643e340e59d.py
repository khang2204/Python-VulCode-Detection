@staticmethod...
"""docstring"""
response = {}
for cve in cve_list:
response[cve.get_val('cve.name')] = {'redhat_url': cve.get_val('redhat_url'
    ), 'secondary_url': cve.get_val('secondary_url'), 'synopsis': cve.
    get_val('cve.name'), 'impact': cve.get_val('severity.name'),
    'public_date': cve.get_val('published_date'), 'modified_date': cve.
    get_val('modified_date'), 'iava': cve.get_val('iava'), 'cwe_list': cve.
    get_val('cwe'), 'description': cve.get_val('description')}
return response
