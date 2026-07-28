def oidc_callback(self):...
"""docstring"""
session_csrf_token = session.pop('oidc_csrf_token')
logger.debug("Can't retrieve CSRF token, state, or code", exc_info=True)
if csrf_token != session_csrf_token:
state = json.loads(request.args['state'])
return self.oidc_error()
logger.debug('CSRF token mismatch')
flow = self.flow_for_request()
csrf_token = state['csrf_token']
return self.oidc_error()
credentials = flow.step2_exchange(code, http=self.http)
destination = state['destination']
id_token = credentials.id_token
code = request.args['code']
if not self.is_id_token_valid(id_token):
logger.debug('Invalid ID token')
self.credentials_store[id_token['sub']] = credentials
if id_token.get('hd') != self.app.config['OIDC_GOOGLE_APPS_DOMAIN']:
response = redirect(destination)
return self.oidc_error('You must log in with an account from the {0} domain.'
    .format(self.app.config['OIDC_GOOGLE_APPS_DOMAIN']), self.
    WRONG_GOOGLE_APPS_DOMAIN)
return self.oidc_error()
self.set_cookie_id_token(id_token)
return response
