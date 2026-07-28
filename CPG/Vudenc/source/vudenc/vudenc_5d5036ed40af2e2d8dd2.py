@mock.patch('requests.post', mock_import_repository_task)...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/config'.format(**locals())
body = {'values': json.dumps({'NEW_URL1': 'http://localhost:8080/'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertIn('NEW_URL1', response.data['values'])
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['count'], 2)
url = '/api/apps/{app_id}/releases/v1'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
release1 = response.data
self.assertIn('config', response.data)
self.assertIn('build', response.data)
self.assertEquals(release1['version'], 1)
self.assertEquals(release1['image'], 'deis/helloworld')
url = '/api/apps/{app_id}/releases/v2'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
release2 = response.data
self.assertNotEqual(release1['uuid'], release2['uuid'])
self.assertNotEqual(release1['config'], release2['config'])
self.assertEqual(release1['build'], release2['build'])
self.assertEquals(release2['version'], 2)
url = '/api/apps/{app_id}/builds'.format(**locals())
build_config = json.dumps({'PATH': 'bin:/usr/local/bin:/usr/bin:/bin'})
body = {'image': 'autotest/example'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertEqual(response.data['image'], body['image'])
url = '/api/apps/{app_id}/releases/v3'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
release3 = response.data
self.assertNotEqual(release2['uuid'], release3['uuid'])
self.assertNotEqual(release2['build'], release3['build'])
self.assertEquals(release3['version'], 3)
url = '/api/apps/{app_id}/releases/v2'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
release2 = response.data
self.assertNotEqual(release2['uuid'], release3['uuid'])
self.assertNotEqual(release2['build'], release3['build'])
self.assertEquals(release2['version'], 2)
url = '/api/apps/{app_id}/releases'.format(**locals())
self.assertEqual(self.client.post(url).status_code, 405)
self.assertEqual(self.client.put(url).status_code, 405)
self.assertEqual(self.client.patch(url).status_code, 405)
self.assertEqual(self.client.delete(url).status_code, 405)
return release3
