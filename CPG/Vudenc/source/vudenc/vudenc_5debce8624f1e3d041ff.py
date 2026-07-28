def test_xsrf_token_identity_matters(self):...
app, calls = self.make_xsrf_handling_app()
self.mock_get_current_identity(model.Identity(model.IDENTITY_USER,
    'a@example.com'))
token = app.get('/request').body
self.mock_get_current_identity(model.Identity(model.IDENTITY_USER,
    'b@example.com'))
response = app.post('/request', expect_errors=True)
self.assertEqual(403, response.status_int)
self.assertFalse(calls)
