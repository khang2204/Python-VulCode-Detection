def test_config_hook(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/config'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertIn('values', response.data)
values = response.data['values']
config = {'username': 'autotest', 'app': app_id}
url = '/api/hooks/config'.format(**locals())
body = {'receive_user': 'autotest', 'receive_repo': app_id}
self.assertIsNone(self.client.logout())
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 403)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json', HTTP_X_DEIS_BUILDER_AUTH=settings.BUILDER_KEY)
self.assertEqual(response.status_code, 200)
self.assertIn('values', response.data)
self.assertEqual(values, response.data['values'])
