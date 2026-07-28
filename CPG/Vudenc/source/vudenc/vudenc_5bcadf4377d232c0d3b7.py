@auth.before_app_request...
if current_user.is_authenticated:
current_user.ping()
if not current_user.verify_auth_token(session['auth_token']):
logout_user()
if not current_user.confirmed and request.endpoint[:5
flash('Your session has expired.')
return redirect(url_for('auth.unconfirmed'))
return redirect(url_for('auth.login'))
