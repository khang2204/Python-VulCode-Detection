def test_xsrf_token_uses_enforce_on(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app(xsrf_token_enforce_on=('PUT',))
token = app.get('/request').body
app.post('/request', {'xsrf_token': token})
app.put('/request', {'xsrf_token': token})
self.assertEqual([('POST', True), ('PUT', True)], calls)
self.assertEqual(200, app.post('/request').status_int)
self.assertEqual(403, app.put('/request', expect_errors=True).status_int)
bad_token = {'xsrf_token': 'boo'}
self.assertEqual(403, app.post('/request', bad_token, expect_errors=True).
    status_int)
self.assertEqual(403, app.put('/request', bad_token, expect_errors=True).
    status_int)
