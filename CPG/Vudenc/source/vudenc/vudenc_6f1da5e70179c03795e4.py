def test_admin_can_see_other_apps(self):...
"""docstring"""
self.assertTrue(self.client.login(username='autotest2', password='password'))
app_id = 'autotest'
url = '/api/apps'
body = {'id': app_id}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertTrue(self.client.login(username='autotest', password='password'))
response = self.client.get(url)
self.assertEqual(response.data['count'], 1)
