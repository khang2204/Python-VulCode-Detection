@mock.patch('requests.post', mock_import_repository_task)...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
build = {'username': 'autotest', 'app': app_id}
url = '/api/hooks/builds'.format(**locals())
body = {'receive_user': 'autotest', 'receive_repo': app_id, 'image':
    '{app_id}:v2'.format(**locals())}
self.assertIsNone(self.client.logout())
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 403)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json', HTTP_X_DEIS_BUILDER_AUTH=settings.BUILDER_KEY)
self.assertEqual(response.status_code, 200)
self.assertIn('release', response.data)
self.assertIn('version', response.data['release'])
self.assertIn('domains', response.data)
