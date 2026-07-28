def test_push_hook(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
body = {'sha': 'df1e628f2244b73f9cdf944f880a2b3470a122f4', 'fingerprint':
    '88:25:ed:67:56:91:3d:c6:1b:7f:42:c6:9b:41:24:80', 'receive_user':
    'autotest', 'receive_repo': '{app_id}'.format(**locals()),
    'ssh_connection': '10.0.1.10 50337 172.17.0.143 22',
    'ssh_original_command': "git-receive-pack '{app_id}.git'".format(**
    locals())}
url = '/api/hooks/push'.format(**locals())
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 403)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json', HTTP_X_DEIS_BUILDER_AUTH=settings.BUILDER_KEY)
self.assertEqual(response.status_code, 201)
for k in ('owner', 'app', 'sha', 'fingerprint', 'receive_repo',
self.assertIn(k, response.data)
