def test_xsrf_token_get_param(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app()
token = app.get('/request').body
app.post('/request?xsrf_token=%s' % token)
self.assertEqual([('POST', True)], calls)
