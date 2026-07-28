def test_run_without_auth(self):...
"""docstring"""
settings.SSH_PRIVATE_KEY = ''
url = '/api/apps'
body = {'id': 'autotest'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/run'.format(**locals())
body = {'command': 'ls -al'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEquals(response.status_code, 400)
self.assertEquals(response.data, 'Support for admin commands is not configured'
    )
