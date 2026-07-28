def test_xsrf_token_post_param(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app()
token = app.get('/request').body
app.post('/request', {'xsrf_token': token})
self.assertEqual([('POST', True)], calls)
