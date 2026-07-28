def test_app_actions(self):...
url = '/api/apps'
body = {'id': 'autotest'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
if not os.path.exists(settings.DEIS_LOG_DIR):
os.mkdir(settings.DEIS_LOG_DIR)
path = os.path.join(settings.DEIS_LOG_DIR, app_id + '.log')
if os.path.exists(path):
os.remove(path)
url = '/api/apps/{app_id}/logs'.format(**locals())
response = self.client.get(url)
self.assertEqual(response.status_code, 204)
self.assertEqual(response.data, 'No logs for {}'.format(app_id))
f.write(FAKE_LOG_DATA)
response = self.client.get(url)
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data, FAKE_LOG_DATA)
os.remove(path)
url = '/api/apps/{app_id}/run'.format(**locals())
body = {'command': 'ls -al'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 200)
self.assertEqual(response.data[0], 0)
os.remove(path)
