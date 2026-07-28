def authenticate_or_redirect(self):...
"""docstring"""
if request.endpoint in frozenset(['oidc_callback', 'oidc_error']):
return None
id_token = self.get_cookie_id_token()
if id_token is None:
return self.redirect_to_auth_server(request.url)
if self.time() >= id_token['exp']:
g.oidc_id_token = id_token
credentials = self.credentials_store[id_token['sub']]
logger.debug('Expired ID token, credentials missing', exc_info=True)
credentials.refresh(self.http)
logger.debug("Expired ID token, can't refresh credentials", exc_info=True)
return None
return self.redirect_to_auth_server(request.url)
id_token = credentials.id_token
return self.redirect_to_auth_server(request.url)
self.credentials_store[id_token['sub']] = credentials
self.set_cookie_id_token(id_token)
