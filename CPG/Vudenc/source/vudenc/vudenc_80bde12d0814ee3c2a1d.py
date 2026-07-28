def _select2_list(search_results):...
select2_results = []
for r in search_results:
select2_results.append({'id': r.id, 'text': r.text})
return select2_results
