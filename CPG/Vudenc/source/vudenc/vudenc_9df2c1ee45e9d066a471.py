def test_x_deis_version_header_not_present(self):...
"""docstring"""
response = self.client.get('/api/apps')
self.assertEqual(response.status_code, 200)
