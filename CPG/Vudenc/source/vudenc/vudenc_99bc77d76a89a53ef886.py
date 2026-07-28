async def test_positive_load_dataset(test_cli):...
import csv
headers = {'Authorization': f'Bearer {access_token}'}
dsreader = csv.reader(open('jogging_dataset.csv'), delimiter=',')
for row in dsreader:
data = {'date': row[0], 'location': row[1], 'distance': int(row[2]), 'time':
    int(row[3])}
resp = await test_cli.post('/results', headers=headers, data=json.dumps(data))
assert resp.status == 201
