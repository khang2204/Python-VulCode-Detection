def test_container_api_heroku(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 0)
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 4, 'worker': 2}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 6)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
url = '/api/apps/{app_id}/containers/web'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 4)
num = response.data['results'][0]['num']
url = '/api/apps/{app_id}/containers/web/{num}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['num'], num)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 2, 'worker': 1}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 3)
self.assertEqual(max(c['num'] for c in response.data['results']), 2)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 0, 'worker': 0}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 0)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
