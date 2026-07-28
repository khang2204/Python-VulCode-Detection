def test_x_deis_version_header_bad(self):...
"""docstring"""
response = self.client.get('/api/apps', HTTP_X_DEIS_VERSION='1234.5678')
self.assertEqual(response.status_code, 405)
