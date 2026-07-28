@oauth_error_handler...
"""docstring"""
if not current_user.is_authenticated():
return current_app.login_manager.unauthorized()
account = RemoteAccount.get(user_id=current_user.get_id(), client_id=remote
    .consumer_key)
if account:
account.delete()
return redirect(url_for('oauthclient_settings.index'))
