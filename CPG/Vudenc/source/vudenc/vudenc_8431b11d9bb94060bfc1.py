async def test_negative_jogging_result(test_cli):...
headers = {'Authorization': f'Bearer {access_token}'}
data = {'date': '1971-06-20', 'distance': 2000, 'time': 405, 'location':
    '32.0853 34.7818'}
resp = await test_cli.post('/results', headers=headers, data=json.dumps(data))
assert resp.status == 400
