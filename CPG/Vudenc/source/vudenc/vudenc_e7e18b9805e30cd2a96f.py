def clean_database(solr):...
url = solr + '/solr/possible.conflicts/update?commit=true'
headers = {'content-type': 'text/xml'}
data = '<delete><query>id:*</query></delete>'
r = requests.post(url, headers=headers, data=data)
assert r.status_code == 200
