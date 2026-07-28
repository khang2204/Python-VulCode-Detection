def _check_key(self, pubkey):...
"""docstring"""
url = '/api/keys'
body = {'id': 'mykey@box.local', 'public': pubkey}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
key_id = response.data['id']
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
url = '/api/keys/{key_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(body['id'], response.data['id'])
self.assertEqual(body['public'], response.data['public'])
response = self.client.delete(url)
self.assertEqual(response.status_code, 204)
