async def test_positive_get_paging(test_cli):...
headers = {'Authorization': f'Bearer {access_token}'}
resp = await test_cli.get('/results?page=0&count=2', headers=headers)
resp_json = await resp.json()
assert resp.status == 200
assert len(resp_json) == 2
resp = await test_cli.get('/results?page=1&count=1', headers=headers)
resp_json = await resp.json()
assert resp.status == 200
assert len(resp_json) == 1
