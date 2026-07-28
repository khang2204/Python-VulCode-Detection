@authn_views.route('/saml2-ls', methods=['POST'])...
"""docstring"""
current_app.logger.debug('Logout service started')
state = StateCache(session)
identity = IdentityCache(session)
client = Saml2Client(current_app.saml2_config, state_cache=state,
    identity_cache=identity)
logout_redirect_url = current_app.config.get('SAML2_LOGOUT_REDIRECT_URL')
next_page = session.get('next', logout_redirect_url)
next_page = request.args.get('next', next_page)
next_page = request.form.get('RelayState', next_page)
if 'SAMLResponse' in request.form:
current_app.logger.debug('Receiving a logout response from the IdP')
if 'SAMLRequest' in request.form:
response = client.parse_logout_request_response(request.form['SAMLResponse'
    ], BINDING_HTTP_REDIRECT)
current_app.logger.debug('Receiving a logout request from the IdP')
current_app.logger.error('No SAMLResponse or SAMLRequest parameter found')
state.sync()
subject_id = _get_name_id(session)
abort(400)
if response and response.status_ok():
if subject_id is None:
session.clear()
current_app.logger.error('Unknown error during the logout')
current_app.logger.warning(
    'The session does not contain the subject id for user {0} Performing local logout'
    .format(session['eduPersonPrincipalName']))
http_info = client.handle_logout_request(request.form['SAMLRequest'],
    subject_id, BINDING_HTTP_REDIRECT, relay_state=request.form['RelayState'])
return redirect(next_page)
abort(400)
session.clear()
state.sync()
return redirect(next_page)
location = get_location(http_info)
session.clear()
return redirect(location)
