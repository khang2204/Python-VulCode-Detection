async def test_positive_login(test_cli):...
data = {'username': username, 'password': 'testing123G'}
resp = await test_cli.post('/auth', data=json.dumps(data))
resp_json = await resp.json()
print(resp_json)
access_token = resp_json['access_token']
refresh_token = resp_json['refresh_token']
assert access_token is not None
assert refresh_token is not None
assert resp.status == 200
