def _reauthn(reason, session_info, user):...
current_app.logger.info('Reauthenticating user {!r} for {!r}.'.format(user,
    reason))
session['_saml2_session_name_id'] = code(session_info['name_id'])
session[reason] = int(time())
session.persist()
relay_state = request.form.get('RelayState', '/')
current_app.logger.debug('Redirecting to the RelayState: ' + relay_state)
return redirect(location=relay_state)
