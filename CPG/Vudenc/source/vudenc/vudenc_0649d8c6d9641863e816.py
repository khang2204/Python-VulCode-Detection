def get_solr_result(index, params):...
"""docstring"""
params = urlencode(params)
result = requests.get('http://%s/solr/biblio/select?%s' % (index, params))
return result.json()
