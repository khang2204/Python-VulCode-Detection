async def test_positive_register_(test_cli):...
data = {'username': username, 'password': 'testing123G'}
resp = await test_cli.post('/users', data=json.dumps(data))
assert resp.status == 201
