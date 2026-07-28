def test_no_remote_app(self):...
self.assert404(self.client.get(url_for('oauthclient.authorized', remote_app
    ='invalid')))
self.assert404(self.client.get(url_for('oauthclient.disconnect', remote_app
    ='invalid')))
