def mock_response(self, app='test', data=None):...
"""docstring"""
from invenio.modules.oauthclient.client import oauth
oauth.remote_apps[app].handle_oauth2_response = MagicMock(return_value=data or
    {'access_token': 'test_access_token', 'scope': '', 'token_type': 'bearer'})
