def test_app_errors(self):...
app_id = 'autotest-errors'
url = '/api/apps'
body = {'id': 'camelCase'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertContains(response, 'App IDs can only contain [a-z0-9-]',
    status_code=400)
url = '/api/apps'
body = {'id': 'deis'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertContains(response, "App IDs cannot be 'deis'", status_code=400)
body = {'id': app_id}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.delete(url)
self.assertEquals(response.status_code, 204)
for endpoint in ('containers', 'config', 'releases', 'builds'):
url = '/api/apps/{app_id}/{endpoint}'.format(**locals())
response = self.client.get(url)
self.assertEquals(response.status_code, 404)
