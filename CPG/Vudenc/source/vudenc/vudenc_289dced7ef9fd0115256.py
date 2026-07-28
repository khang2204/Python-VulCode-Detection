def test_authorized(self):...
c.get(url_for('oauthclient.login', remote_app='test'))
self.mock_response(app='test')
self.mock_response(app='test_invalid')
resp = c.get(url_for('oauthclient.authorized', remote_app='test', code='test'))
assert resp.data == 'TEST'
assert self.handled_remote.name == 'test'
assert not self.handled_args
assert not self.handled_kwargs
assert self.handled_resp['access_token'] == 'test_access_token'
resp = self.assertRaises(TypeError, c.get, url_for('oauthclient.authorized',
    remote_app='test_invalid', code='test'))
