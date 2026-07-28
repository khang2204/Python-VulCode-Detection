@mock.patch('requests.post', mock_import_repository_task)...
"""docstring"""
self.client.login(username='autotest2', password='password')
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
self.client.login(username='autotest', password='password')
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
