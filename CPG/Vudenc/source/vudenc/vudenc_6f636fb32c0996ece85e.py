async def test_negative_bad_paging(test_cli):...
headers = {'Authorization': f'Bearer {access_token}'}
resp = await test_cli.get('/results?page=-1&count=2', headers=headers)
assert resp.status == 400
resp = await test_cli.get('/results?page=1&count=0', headers=headers)
assert resp.status == 400
