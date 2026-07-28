def test_admin_can_manage_other_apps(self):...
"""docstring"""
self.assertTrue(self.client.login(username='autotest2', password='password'))
app_id = 'autotest'
url = '/api/apps'
body = {'id': app_id}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertTrue(self.client.login(username='autotest', password='password'))
url = '/api/apps/{}'.format(app_id)
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
url = '/api/apps/{app_id}/logs'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertIn('autotest2 created initial release', response.data)
url = '/api/apps/{app_id}/run'.format(**locals())
body = {'command': 'ls -al'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data[0], 0)
url = '/api/apps/{}'.format(app_id)
response = self.client.delete(url)
self.assertEqual(response.status_code, 204)
