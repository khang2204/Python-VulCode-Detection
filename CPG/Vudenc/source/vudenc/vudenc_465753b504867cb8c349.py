def test_create_errors(self):...
response = self.client.get('/api/apps')
app_id = response.data['results'][0]['id']
self.assertTrue(self.client.login(username='autotest-2', password='password'))
url = '/api/apps/{}/perms'.format(app_id)
body = {'username': 'autotest-2'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 403)
