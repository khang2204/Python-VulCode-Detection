def test_authn(self):...
resp = c.get('/test2')
self.assertEqual(resp.status_code, 302)
self.assertTrue(resp.location.startswith(self.app.config['TOKEN_SERVICE_URL']))
