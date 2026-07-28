@pytest.fixture(scope='session', autouse=True)...
url = solr + '/solr/admin/cores?action=RELOAD&core=possible.conflicts&wt=json'
r = requests.get(url)
assert r.status_code == 200
