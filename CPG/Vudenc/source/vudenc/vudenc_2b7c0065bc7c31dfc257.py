async def test_positive_get_all_results(test_cli):...
headers = {'Authorization': f'Bearer {access_token}'}
resp = await test_cli.get('/results', headers=headers)
resp_json = await resp.json()
assert resp.status == 200
