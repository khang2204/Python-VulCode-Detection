@mock.patch('requests.post', mock_import_repository_task)...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
build = Build.objects.get(uuid=response.data['uuid'])
self.assertEqual(str(build), '{}-{}'.format(response.data['app'], response.
    data['uuid'][:7]))
