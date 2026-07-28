@patch('invenio.ext.session.interface.SessionInterface.save_session')...
from invenio.modules.oauthclient.models import RemoteToken
from invenio.modules.oauthclient.handlers import token_getter
from invenio.modules.oauthclient.client import oauth
user = MagicMock()
user.get_id = MagicMock(return_value=1)
user.is_authenticated = MagicMock(return_value=True)
res = c.get(url_for('oauthclient.login', remote_app='full'))
assert res.status_code == 302
assert res.location.startswith(oauth.remote_apps['full'].authorize_url)
self.mock_response(app='full')
c.get(url_for('oauthclient.authorized', remote_app='full', code='test'))
assert session['oauth_token_full'] == ('test_access_token', '')
t = RemoteToken.get(1, 'fullid')
assert t.remote_account.client_id == 'fullid'
assert t.access_token == 'test_access_token'
assert RemoteToken.query.count() == 1
self.mock_response(app='full', data={'access_token': 'new_access_token',
    'scope': '', 'token_type': 'bearer'})
c.get(url_for('oauthclient.authorized', remote_app='full', code='test'))
t = RemoteToken.get(1, 'fullid')
assert t.access_token == 'new_access_token'
assert RemoteToken.query.count() == 1
val = token_getter(oauth.remote_apps['full'])
assert val == ('new_access_token', '')
res = c.get(url_for('oauthclient.disconnect', remote_app='full'))
assert res.status_code == 302
assert res.location.endswith(url_for('oauthclient_settings.index'))
t = RemoteToken.get(1, 'fullid')
assert t is None
