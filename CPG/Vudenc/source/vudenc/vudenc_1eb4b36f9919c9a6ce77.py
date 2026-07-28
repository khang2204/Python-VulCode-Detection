def get_all_current_sources(k10plus, ai):...
"""docstring"""
params = {'facet': 'true', 'facet.field': 'source_id', 'facet.mincount': 3,
    'q': '!source_id:error', 'rows': 0, 'wt': 'json'}
result = get_solr_result(k10plus, params)
k10plus_sources = result['facet_counts']['facet_fields']['source_id']
k10plus_sources = set([int(sid) for sid in k10plus_sources[::2]])
result = get_solr_result(ai, params)
ai_sources = result['facet_counts']['facet_fields']['source_id']
ai_sources = set([int(sid) for sid in ai_sources[::2]])
shared = k10plus_sources.intersection(ai_sources)
if len(shared) > 0:
ssid = [str(sid) for sid in shared]
return k10plus_sources.union(ai_sources)
message = (
    'Die folgenden Quellen befinden sich sowohl im K10plus als auch im AI: {}'
    .format(', '.join(ssid)))
send_message(message)
