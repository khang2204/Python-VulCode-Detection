@patch('invenio.ext.session.interface.SessionInterface.save_session')...
from invenio.modules.oauthclient.client import oauth
user = MagicMock()
user.get_id = MagicMock(return_value=1)
user.is_authenticated = MagicMock(return_value=True)
res = c.get(url_for('oauthclient.login', remote_app='full'))
assert res.status_code == 302
assert res.location.startswith(oauth.remote_apps['full'].authorize_url)
self.mock_response(app='full', data=dict(error_uri=
    'http://developer.github.com/v3/oauth/#bad-verification-code',
    error_description='The code passed is incorrect or expired.', error=
    'bad_verification_code'))
res = c.get(url_for('oauthclient.authorized', remote_app='full', code='test'))
assert res.status_code == 302
