def test_create(self):...
submit = {'username': 'first', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
submit = {'username': 'second', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
self.assertTrue(self.client.login(username='first', password='password'))
url = '/api/admin/perms'
body = {'username': 'second'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
self.assertIn('second', str(response.data['results']))
