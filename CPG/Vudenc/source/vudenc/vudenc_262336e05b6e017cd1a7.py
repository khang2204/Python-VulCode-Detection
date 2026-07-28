@authn_views.route('/token-login', methods=['POST'])...
current_app.logger.debug('Starting token login')
location_on_fail = current_app.config.get('TOKEN_LOGIN_FAILURE_REDIRECT_URL')
location_on_success = current_app.config.get('TOKEN_LOGIN_SUCCESS_REDIRECT_URL'
    )
eppn = request.form.get('eppn')
token = request.form.get('token')
nonce = request.form.get('nonce')
timestamp = request.form.get('ts')
loa = get_loa(current_app.config.get('AVAILABLE_LOA'), None)
if verify_auth_token(eppn=eppn, token=token, nonce=nonce, timestamp=timestamp):
current_app.logger.info('Token login failed, redirecting user to {}'.format
    (location_on_fail))
user = current_app.central_userdb.get_user_by_eppn(eppn)
current_app.logger.error('No user with eduPersonPrincipalName = {} found'.
    format(eppn))
return redirect(location_on_fail)
if user.locked_identity.count > 0:
current_app.logger.error(
    'There are more than one user with eduPersonPrincipalName = {}'.format(
    eppn))
current_app.logger.error('Not new user {} tried to log in using token login'
    .format(user))
session['eduPersonPrincipalName'] = user.eppn
return redirect(location_on_fail)
session['user_eppn'] = user.eppn
session['eduPersonAssurance'] = loa
session.persist()
response = redirect(location_on_success)
session.set_cookie(response)
current_app.logger.info('Successful token login, redirecting user {} to {}'
    .format(user, location_on_success))
return response
