@mock.patch('requests.post', mock_import_repository_task)...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/releases/rollback/'.format(**locals())
response = self.client.post(url, content_type='application/json')
self.assertEqual(response.status_code, 404)
url = '/api/apps/{app_id}/config'.format(**locals())
body = {'values': json.dumps({'NEW_URL1': 'http://localhost:8080/'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/builds'.format(**locals())
build_config = json.dumps({'PATH': 'bin:/usr/local/bin:/usr/bin:/bin'})
body = {'image': 'autotest/example'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/releases/rollback/'.format(**locals())
response = self.client.post(url, content_type='application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url, content_type='application/json')
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['count'], 4)
url = '/api/apps/{app_id}/releases/v2'.format(**locals())
response = self.client.get(url, content_type='application/json')
self.assertEqual(response.status_code, 200)
release2 = response.data
self.assertEquals(release2['version'], 2)
url = '/api/apps/{app_id}/releases/v4'.format(**locals())
response = self.client.get(url, content_type='application/json')
self.assertEqual(response.status_code, 200)
release4 = response.data
self.assertEquals(release4['version'], 4)
self.assertNotEqual(release2['uuid'], release4['uuid'])
self.assertEqual(release2['build'], release4['build'])
self.assertEqual(release2['config'], release4['config'])
url = '/api/apps/{app_id}/releases/rollback/'.format(**locals())
body = {'version': 1}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/releases'.format(**locals())
response = self.client.get(url, content_type='application/json')
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['count'], 5)
url = '/api/apps/{app_id}/releases/v1'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
release1 = response.data
url = '/api/apps/{app_id}/releases/v5'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
release5 = response.data
self.assertEqual(release5['version'], 5)
self.assertNotEqual(release1['uuid'], release5['uuid'])
self.assertEqual(release1['build'], release5['build'])
self.assertEqual(release1['config'], release5['config'])
url = '/api/apps/{app_id}/config'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data['values'], {})
url = '/api/apps/{app_id}/releases/rollback/'.format(**locals())
body = {'version': 3}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/config'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
values = response.data['values']
self.assertIn('NEW_URL1', values)
self.assertEqual('http://localhost:8080/', values['NEW_URL1'])
