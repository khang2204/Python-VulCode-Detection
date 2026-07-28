def _get_fast_results(term, index='suggestall'):...
error_response = [{'text': 'FAST results', 'children': [{'id': '', 'text':
    'Error retrieving FAST results.'}]}]
url = _build_fast_url(term, index)
r = requests.get(url, timeout=2)
logger.error('fast lookup timed out')
select2_results = _fast_results_to_select2_list(r.json()['response']['docs'
    ], index)
logger.error('fast data exception: %s' % e)
return error_response
if select2_results:
logger.error('fast response: %s - %s' % (r.status_code, r.text))
return [{'text': 'FAST results', 'children': select2_results}]
return []
return error_response
