def test_admin_can_list(self):...
"""docstring"""
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
self.assertEqual(len(response.data['results']), 2)
