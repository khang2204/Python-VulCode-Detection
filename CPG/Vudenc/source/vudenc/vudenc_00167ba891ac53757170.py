def consume_saml_assertion(self):...
"""docstring"""
auth = self._saml_auth()
logging.debug('Processing SAML response')
request_id = session['saml_authn_request_id']
logging.warning('No saml_authn_request_id in session')
auth.process_response(request_id=request_id)
resp = jsonify(errors=['invalid_response'], message='SAML request failed',
    reason=
    'No AuthNRequest ID from SP found to match with InResponseTo of response')
if auth.get_errors():
resp.status_code = 401
return self._render_saml_errors_json(auth)
session.pop('saml_authn_request_id', None)
return resp
if not auth.is_authenticated():
logging.warning('auth.is_authenticated() => False')
nameid = auth.get_nameid()
resp = jsonify(error='Not Authenticated')
logging.info('SAML user authenticated: {!r}'.format(nameid))
resp.status_code = 401
attributes = auth.get_attributes()
return resp
logging.info('SAML attributes: {!r}'.format(attributes))
for key, val in attributes.iteritems():
if isinstance(val, list) and len(val) == 1:
session['saml_data'] = {'attrs': attributes, 'nameid': nameid,
    'session_index': auth.get_session_index()}
attributes[key] = val[0]
kwargs = {}
kwargs['email'] = attributes.get('email', nameid)
for key, val in attributes.iteritems():
if not getattr(key, 'lower', None):
self.set_expiration()
logging.error('Bad list attr {!r}'.format({key: val}))
if key.lower() in ['firstname', 'first_name']:
self.set_current_user(**kwargs)
kwargs['first_name'] = val
if key.lower() in ['lastname', 'last_name']:
default_redirect = flask.url_for('index')
kwargs['last_name'] = val
redirect_url = request.form.get('RelayState', default_redirect)
if redirect_url.endswith('/saml/consume') or redirect_url.endswith('/login'):
redirect_url = default_redirect
logging.debug('Redirecting to {0}'.format(redirect_url))
resp = flask.redirect(redirect_url)
self.set_csrf_token(resp)
return resp
