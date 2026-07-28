def _authn(action, force_authn=False):...
redirect_url = current_app.config.get('SAML2_LOGIN_REDIRECT_URL', '/')
relay_state = request.args.get('next', redirect_url)
idps = current_app.saml2_config.getattr('idp')
assert len(idps) == 1
idp = idps.keys()[0]
idp = request.args.get('idp', idp)
loa = request.args.get('required_loa', None)
authn_request = get_authn_request(current_app.config, session, relay_state,
    idp, required_loa=loa, force_authn=force_authn)
schedule_action(action)
current_app.logger.info('Redirecting the user to the IdP for ' + action)
return redirect(get_location(authn_request))
