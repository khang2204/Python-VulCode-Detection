def seed_database_with(solr, name, id='1', source='CORP'):...
url = solr + '/solr/possible.conflicts/update?commit=true'
headers = {'content-type': 'application/json'}
data = ('[{"source":"' + source + '", "name":"' + name + '", "id":"' + id +
    '"}]')
r = requests.post(url, headers=headers, data=data)
assert r.status_code == 200
