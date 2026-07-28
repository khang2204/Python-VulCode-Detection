def test_build_hook_procfile(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
build = {'username': 'autotest', 'app': app_id}
url = '/api/hooks/builds'.format(**locals())
PROCFILE = {'web': 'node server.js', 'worker': 'node worker.js'}
SHA = 'ecdff91c57a0b9ab82e89634df87e293d259a3aa'
body = {'receive_user': 'autotest', 'receive_repo': app_id, 'image':
    '{app_id}:v2'.format(**locals()), 'sha': SHA, 'procfile': PROCFILE}
self.assertIsNone(self.client.logout())
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 403)
response = self.client.post(url, json.dumps(body), content_type=
    'application/json', HTTP_X_DEIS_BUILDER_AUTH=settings.BUILDER_KEY)
self.assertEqual(response.status_code, 200)
self.assertIn('release', response.data)
self.assertIn('version', response.data['release'])
self.assertIn('domains', response.data)
self.assertTrue(self.client.login(username='autotest', password='password'))
url = '/api/apps/{app_id}/builds'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertIn('results', response.data)
build = response.data['results'][0]
self.assertEqual(build['sha'], SHA)
self.assertEqual(build['procfile'], PROCFILE)
url = '/api/apps/{app_id}/containers/web'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 1)
container = response.data['results'][0]
self.assertEqual(container['type'], 'web')
self.assertEqual(container['num'], 1)
