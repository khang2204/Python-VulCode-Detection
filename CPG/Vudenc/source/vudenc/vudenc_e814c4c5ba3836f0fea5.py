def test_list(self):...
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
app_id = response.data['results'][0]['id']
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.get('/api/apps/{}/perms'.format(app_id),
    content_type='application/json')
self.assertEqual(response.data, {'users': ['autotest-2']})
