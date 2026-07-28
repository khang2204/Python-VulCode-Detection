def test_app(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
self.assertIn('id', response.data)
self.assertIn('url', response.data)
self.assertEqual(response.data['url'], '{app_id}.deisapp.local'.format(**
    locals()))
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
body = {'id': 'new'}
response = self.client.patch(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 405)
response = self.client.delete(url)
self.assertEqual(response.status_code, 204)
