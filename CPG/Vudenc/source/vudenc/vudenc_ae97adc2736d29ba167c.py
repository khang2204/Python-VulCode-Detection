@mock.patch('requests.post', mock_import_repository_task)...
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
body = {'web': 1}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
self.assertEqual(response.data['results'][0]['release'], 'v2')
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertEqual(response.data['image'], body['image'])
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
self.assertEqual(response.data['results'][0]['release'], 'v3')
url = '/api/apps/{app_id}/config'.format(**locals())
body = {'values': json.dumps({'KEY': 'value'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
self.assertEqual(response.data['results'][0]['release'], 'v4')
