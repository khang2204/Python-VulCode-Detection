def test_no_authn_util(self):...
no_authn_urls_before = [path for path in self.app.config['NO_AUTHN_URLS']]
no_authn_path = '/test3'
no_authn_views(self.app, [no_authn_path])
self.assertEqual(no_authn_urls_before + ['^{!s}$'.format(no_authn_path)],
    self.app.config['NO_AUTHN_URLS'])
resp = c.get('/test3')
self.assertEqual(resp.status_code, 200)
