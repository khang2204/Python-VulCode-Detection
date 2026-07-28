def test_admin_can_manage_other_containers(self):...
"""docstring"""
self.client.login(username='autotest2', password='password')
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'sha': 'a' * 40, 'procfile': json.
    dumps({'web': 'node server.js', 'worker': 'node worker.js'})}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
self.client.login(username='autotest', password='password')
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 4, 'worker': 2}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
