def test_xsrf_token_uses_xsrf_token_request_param(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app(xsrf_token_request_param='tok')
token = app.get('/request').body
app.post('/request', {'tok': token})
self.assertEqual([('POST', True)], calls)
