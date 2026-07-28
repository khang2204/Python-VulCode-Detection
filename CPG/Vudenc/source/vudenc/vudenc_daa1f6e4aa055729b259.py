def test_first_signup(self):...
username, password = 'firstuser', 'password'
email = 'autotest@deis.io'
submit = {'username': username, 'password': password, 'email': email}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
username, password = 'seconduser', 'password'
email = 'autotest@deis.io'
submit = {'username': username, 'password': password, 'email': email}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
