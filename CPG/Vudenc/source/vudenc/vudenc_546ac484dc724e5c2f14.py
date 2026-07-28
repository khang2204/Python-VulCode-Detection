@mock.patch('requests.post', mock_import_repository_task)...
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 0)
url = '/api/apps/{app_id}/builds'.format(**locals())
body = {'image': 'autotest/example', 'dockerfile':
    """FROM busybox
CMD /bin/true"""}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'cmd': 6}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 6)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
url = '/api/apps/{app_id}/containers/cmd'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 6)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'cmd': 3}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 3)
self.assertEqual(max(c['num'] for c in response.data['results']), 3)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
url = '/api/apps/{app_id}/scale'.format(**locals())
body = {'cmd': 0}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 204)
url = '/api/apps/{app_id}/containers'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 0)
url = '/api/apps/{app_id}'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
