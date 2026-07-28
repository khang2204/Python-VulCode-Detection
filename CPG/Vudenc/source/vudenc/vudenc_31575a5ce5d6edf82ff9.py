def test_container_errors(self):...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'web': 'not_an_int'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertContains(response, 'Invalid scaling format', status_code=400)
body = {'invalid': 1}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertContains(response, 'Container type invalid', status_code=400)
