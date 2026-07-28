def test_create(self):...
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
app_id = response.data['results'][0]['id']
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps')
self.assertEqual(len(response.data['results']), 1)
for model in ['builds', 'config', 'containers', 'limits', 'releases']:
response = self.client.get('/api/apps/{}/{}/'.format(app_id, model))
self.assertTrue(self.client.login(username='autotest-1', password='password'))
self.assertEqual(response.data['detail'], 'Not found')
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
for model in ['builds', 'containers', 'releases']:
response = self.client.get('/api/apps/{}/{}/'.format(app_id, model))
self.assertEqual(len(response.data['results']), 0)
