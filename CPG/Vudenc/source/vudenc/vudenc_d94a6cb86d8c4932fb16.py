def test_app_release_notes_in_logs(self):...
"""docstring"""
url = '/api/apps'
body = {'id': 'autotest'}
response = self.client.post(url, json.dumps(body), content_type=
    'application/json')
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
path = os.path.join(settings.DEIS_LOG_DIR, app_id + '.log')
url = '/api/apps/{app_id}/logs'.format(**locals())
response = self.client.get(url)
self.assertIn('autotest created initial release', response.data)
self.assertEqual(response.status_code, 200)
os.remove(path)
