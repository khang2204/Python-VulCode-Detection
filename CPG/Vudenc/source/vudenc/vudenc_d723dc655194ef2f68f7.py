@authn_views.route('/logout', methods=['POST'])...
"""docstring"""
eppn = session.get('user_eppn')
if eppn is None:
current_app.logger.info('Session cookie has expired, no logout action needed')
user = current_app.central_userdb.get_user_by_eppn(eppn)
location = current_app.config.get('SAML2_LOGOUT_REDIRECT_URL')
current_app.logger.debug('Logout process started for user {!r}'.format(user))
return LogoutPayload().dump({'location': location}).data
state = StateCache(session)
identity = IdentityCache(session)
client = Saml2Client(current_app.saml2_config, state_cache=state,
    identity_cache=identity)
subject_id = _get_name_id(session)
if subject_id is None:
current_app.logger.warning(
    'The session does not contain the subject id for user {!r}'.format(user))
logouts = client.global_logout(subject_id)
location = current_app.config.get('SAML2_LOGOUT_REDIRECT_URL')
loresponse = logouts.values()[0]
state.sync()
if isinstance(loresponse, LogoutResponse):
return LogoutPayload().dump({'location': location}).data
if loresponse.status_ok():
headers_tuple = loresponse[1]['headers']
current_app.logger.debug('Performing local logout for {!r}'.format(user))
abort(500)
location = headers_tuple[0][1]
session.clear()
current_app.logger.info(
    'Redirecting to {!r} to continue the logout process for user {!r}'.
    format(location, user))
location = current_app.config.get('SAML2_LOGOUT_REDIRECT_URL')
location = request.form.get('RelayState', location)
return LogoutPayload().dump({'location': location}).data
