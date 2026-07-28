def test_list_errors(self):...
response = self.client.get('/api/apps')
app_id = response.data['results'][0]['id']
self.assertTrue(self.client.login(username='autotest-2', password='password'))
response = self.client.get('/api/apps/{}/perms'.format(app_id),
    content_type='application/json')
self.assertEqual(response.status_code, 403)
