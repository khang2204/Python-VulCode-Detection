def test_settings_view(self):...
from invenio.modules.oauthclient.models import RemoteAccount
RemoteAccount.create(1, 'testid', None)
self.assert401(self.client.get(url_for('oauthclient_settings.index'),
    follow_redirects=True))
self.login('admin', '')
res = self.client.get(url_for('oauthclient_settings.index'))
self.assert200(res)
assert 'MyLinkedTestAccount' in res.data
assert url_for('oauthclient.disconnect', remote_app='test') in res.data
assert url_for('oauthclient.login', remote_app='full') in res.data
assert url_for('oauthclient.login', remote_app='test_invalid') in res.data
