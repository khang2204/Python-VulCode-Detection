def test_no_cookie(self):...
resp = c.get('/')
self.assertEqual(resp.status_code, 302)
self.assertTrue(resp.location.startswith(self.app.config['TOKEN_SERVICE_URL']))
