def test_login(self):...
resp = self.client.get(url_for('oauthclient.login', remote_app='test'))
self.assertStatus(resp, 302)
self.assertEqual(resp.location, 
    'https://foo.bar/oauth/authorize?response_type=code&client_id=testid&redirect_uri=%s'
     % quote_plus(url_for('oauthclient.authorized', remote_app='test',
    _external=True)))
resp = self.client.get(url_for('oauthclient.login', remote_app='invalid'))
self.assertStatus(resp, 404)
