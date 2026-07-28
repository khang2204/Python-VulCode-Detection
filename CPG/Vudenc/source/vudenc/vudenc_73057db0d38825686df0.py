def test_xsrf_token_uses_xsrf_token_header(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app(xsrf_token_header='X-Some')
token = app.get('/request').body
app.post('/request', headers={'X-Some': token})
self.assertEqual([('POST', True)], calls)
