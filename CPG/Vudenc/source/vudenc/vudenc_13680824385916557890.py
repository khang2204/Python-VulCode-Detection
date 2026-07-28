def test_xsrf_token_header(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app()
token = app.get('/request').body
app.post('/request', headers={'X-XSRF-Token': token})
self.assertEqual([('POST', True)], calls)
