def _check_duplicate_key(self, pubkey):...
"""docstring"""
url = '/api/keys'
body = {'id': 'mykey@box.local', 'public': pubkey}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 400)
