@acs_action('login-action')...
"""docstring"""
current_app.logger.info('User {!r} logging in.'.format(user))
session['_saml2_session_name_id'] = code(session_info['name_id'])
session['eduPersonPrincipalName'] = user.eppn
session['user_eppn'] = user.eppn
loa = get_loa(current_app.config.get('AVAILABLE_LOA'), session_info)
session['eduPersonAssurance'] = loa
session.persist()
relay_state = request.form.get('RelayState', '/')
current_app.logger.debug('Redirecting to the RelayState: ' + relay_state)
response = redirect(location=relay_state)
session.set_cookie(response)
current_app.logger.info('Redirecting user {!r} to {!r}'.format(user,
    relay_state))
return response
