@mock.patch('requests.post', mock_import_repository_task)...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['count'], 1)
body = {'image': 'autotest/example'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
build_id = response.data['uuid']
build1 = response.data
self.assertEqual(response.data['image'], body['image'])
url = '/api/apps/{app_id}/builds/{build_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
build2 = response.data
self.assertEqual(build1, build2)
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertIn('x-deis-release', response._headers)
build3 = response.data
self.assertEqual(response.data['image'], body['image'])
self.assertNotEqual(build2['uuid'], build3['uuid'])
self.assertEqual(self.client.put(url).status_code, 405)
self.assertEqual(self.client.patch(url).status_code, 405)
self.assertEqual(self.client.delete(url).status_code, 405)
