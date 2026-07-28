async def test_negative_jogging_result_no_uath(test_cli):...
data = {'date': '2015-06-20', 'distance': 2000, 'time': 405, 'location':
    '32.0853 34.7818'}
resp = await test_cli.post('/results', data=json.dumps(data))
assert resp.status == 400
