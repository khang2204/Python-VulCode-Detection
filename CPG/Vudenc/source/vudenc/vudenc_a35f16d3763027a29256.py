async def test_positive_check_filters(test_cli):...
headers = {'Authorization': f'Bearer {access_token}'}
resp = await test_cli.get("/results?page=0&count=2&filter=date eq '2019-07-15'"
    , headers=headers)
resp_json = await resp.json()
assert resp.status == 200
assert len(resp_json) == 1
resp = await test_cli.get(
    "/results?filter=(date lt '2018-01-01') AND (time lt 500)", headers=headers
    )
resp_json = await resp.json()
assert resp.status == 200
assert len(resp_json) == 4
resp = await test_cli.get('/results?filter=distance ne 2000', headers=headers)
resp_json = await resp.json()
assert resp.status == 200
assert len(resp_json) == 8
resp = await test_cli.get(
    '/results?filter=distance ne 2000 and ((time lt 400) and (time gt 390))',
    headers=headers)
resp_json = await resp.json()
assert resp.status == 200
assert len(resp_json) == 0
