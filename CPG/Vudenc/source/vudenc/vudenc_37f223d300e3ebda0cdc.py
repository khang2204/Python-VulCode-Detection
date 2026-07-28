from namex.models import User
import requests
import json
import pytest
from tests.python import integration_solr, integration_synonym_api
import urllib
from hamcrest import *
token_header = {'alg': 'RS256', 'typ': 'JWT', 'kid':
    'flask-jwt-oidc-test-client'}
claims = {'iss': 'https://sso-dev.pathfinder.gov.bc.ca/auth/realms/sbc',
    'sub': '43e6a245-0bf7-4ccf-9bd0-e7fb85fd18cc', 'aud': 'NameX-Dev',
    'exp': 31531718745, 'iat': 1531718745, 'jti':
    'flask-jwt-oidc-test-support', 'typ': 'Bearer', 'username': 'test-user',
    'realm_access': {'roles': ['{}'.format(User.EDITOR), '{}'.format(User.
    APPROVER), 'viewer', 'user']}}
@pytest.fixture(scope='session', autouse=True)...
url = solr + '/solr/admin/cores?action=RELOAD&core=possible.conflicts&wt=json'
r = requests.get(url)
assert r.status_code == 200
@integration_solr...
url = solr + '/solr/possible.conflicts/admin/ping'
r = requests.get(url)
assert r.status_code == 200
def clean_database(solr):...
url = solr + '/solr/possible.conflicts/update?commit=true'
headers = {'content-type': 'text/xml'}
data = '<delete><query>id:*</query></delete>'
r = requests.post(url, headers=headers, data=data)
assert r.status_code == 200
def seed_database_with(solr, name, id='1', source='CORP'):...
url = solr + '/solr/possible.conflicts/update?commit=true'
headers = {'content-type': 'application/json'}
data = ('[{"source":"' + source + '", "name":"' + name + '", "id":"' + id +
    '"}]')
r = requests.post(url, headers=headers, data=data)
assert r.status_code == 200
def verify(data, expected):...
print('Expected: ', expected)
actual = [{'name': doc['name_info']['name']} for doc in data['names']]
print('Actual: ', actual)
assert_that(len(actual), equal_to(len(expected)))
for i in range(len(actual)):
assert_that(actual[i]['name'], equal_to(expected[i]['name']))
def verify_results(client, jwt, query, expected):...
data = search(client, jwt, query)
verify(data, expected)
def search(client, jwt, query):...
token = jwt.create_jwt(claims, token_header)
headers = {'Authorization': 'Bearer ' + token}
url = '/api/v1/requests/phonetics/' + urllib.parse.quote(query) + '/*'
print(url)
rv = client.get(url, headers=headers)
assert rv.status_code == 200
return json.loads(rv.data)
