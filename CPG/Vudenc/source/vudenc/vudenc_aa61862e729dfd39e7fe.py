def _fast_results_to_select2_list(fast_results, index):...
results = []
fast_ids = []
for item in fast_results:
text = item['auth']
return results
if item['type'] != 'auth':
text = '%s (%s)' % (text, item[index][0])
if item['idroot'] not in fast_ids:
results.append({'id': '%s%s%s' % (item['idroot'], ID_VAL_SEPARATOR, item[
    'auth']), 'text': text})
fast_ids.append(item['idroot'])
