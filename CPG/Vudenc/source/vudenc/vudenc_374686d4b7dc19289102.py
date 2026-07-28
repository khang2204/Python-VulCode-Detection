def test_xsrf_token_missing(self):...
"""docstring"""
app, calls = self.make_xsrf_handling_app()
response = app.post('/request', expect_errors=True)
self.assertEqual(403, response.status_int)
self.assertFalse(calls)
