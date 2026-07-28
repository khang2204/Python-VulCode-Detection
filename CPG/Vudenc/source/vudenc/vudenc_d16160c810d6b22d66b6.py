def test_app_structure_is_valid_json(self):...
"""docstring"""
url = '/api/apps'
response = self.client.post(url)
self.assertEqual(response.status_code, 201)
app_id = response.data['id']
self.assertIn('structure', response.data)
self.assertEqual(response.data['structure'], {})
app = App.objects.get(id=app_id)
app.structure = {'web': 1}
app.save()
url = '/api/apps/{}'.format(app_id)
response = self.client.get(url)
self.assertIn('structure', response.data)
self.assertEqual(response.data['structure'], {'web': 1})
