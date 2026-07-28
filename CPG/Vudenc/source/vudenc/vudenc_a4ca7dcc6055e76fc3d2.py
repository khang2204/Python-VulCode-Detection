@integration_solr...
url = solr + '/solr/possible.conflicts/admin/ping'
r = requests.get(url)
assert r.status_code == 200
