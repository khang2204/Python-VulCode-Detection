def test_create_chaos(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 0}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
chaos.CREATE_ERROR_RATE = 0.5
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 20}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 503)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 20)
states = set([c['state'] for c in response.data['results']])
self.assertEqual(states, set(['error', 'created']))
