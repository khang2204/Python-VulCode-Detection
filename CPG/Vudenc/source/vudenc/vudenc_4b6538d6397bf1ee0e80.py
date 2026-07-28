def login_redirect_url(self, return_to='/', auth=None):...
if auth is None:
auth = self._saml_auth()
login_url = auth.login(return_to=return_to)
session['saml_authn_request_id'] = auth.get_last_request_id()
return login_url
