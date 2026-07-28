def test_x_deis_version_header_good(self):...
"""docstring"""
response = self.client.get('/api/apps', HTTP_X_DEIS_VERSION=__version__.
    rsplit('.', 1)[0])
self.assertEqual(response.status_code, 200)
