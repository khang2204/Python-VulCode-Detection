def authn(self, url, force_authn=False):...
"""docstring"""
resp = c.get(url)
authn_req = get_location(get_authn_request(self.app.config, session, '/',
    None, force_authn=force_authn))
idp_url = authn_req.split('?')[0]
self.assertEqual(resp.status_code, 302)
self.assertTrue(resp.location.startswith(idp_url))
