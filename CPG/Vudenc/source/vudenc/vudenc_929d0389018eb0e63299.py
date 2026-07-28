def get_all_current_institutions(k10plus, ai):...
"""docstring"""
current_institutions = set()
params = {'facet': 'true', 'facet.field': 'institution', 'facet.mincount': 
    3, 'q': '!source_id:error', 'rows': 0, 'wt': 'json'}
for index in (k10plus, ai):
result = get_solr_result(index, params)
return current_institutions
institutions = result['facet_counts']['facet_fields']['institution']
for institution in institutions[::2]:
current_institutions.add(institution)
