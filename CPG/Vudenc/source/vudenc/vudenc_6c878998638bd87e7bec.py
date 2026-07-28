def test_list(self):...
submit = {'username': 'firstuser', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertTrue(response.data['is_superuser'])
self.assertTrue(self.client.login(username='firstuser', password='password'))
response = self.client.get('/api/admin/perms', content_type='application/json')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
self.assertEqual(response.data['results'][0]['username'], 'firstuser')
self.assertTrue(response.data['results'][0]['is_superuser'])
submit = {'username': 'seconduser', 'password': 'password', 'email':
    'autotest@deis.io'}
url = '/api/auth/register'
response = self.client.post(url, json.dumps(submit), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.assertFalse(response.data['is_superuser'])
self.assertTrue(self.client.login(username='seconduser', password='password'))
response = self.client.get('/api/admin/perms', content_type='application/json')
self.assertEqual(response.status_code, 403)
self.assertIn('You do not have permission', response.data['detail'])
