def test_app_override_id(self):...
body = {'id': 'myid'}
response = self.client.post('/api/apps', json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
body = {'id': response.data['id']}
response = self.client.post('/api/apps', json.dumps(body), content_type=
    'application/json')
self.assertContains(response, 'App with this Id already exists.',
    status_code=400)
return response
