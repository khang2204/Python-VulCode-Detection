@oauth_error_handler...
"""docstring"""
session.pop(token_session_key(remote.name) + '_autoregister', None)
token = response_token_setter(remote, resp)
handlers = signup_handlers[remote.name]
if not current_user.is_authenticated():
account_info = handlers['info'](resp)
if not token.remote_account.extra_data and remote.name in signup_handlers:
user = oauth_get_user(remote.consumer_key, account_info=account_info,
    access_token=token_getter(remote)[0])
handlers['setup'](token)
if request.args.get('next', None):
if user is None:
return redirect(request.args.get('next'))
return redirect('/')
user = oauth_register(account_info)
if not oauth_authenticate(remote.consumer_key, user, require_existing_link=
if user is None:
return current_app.login_manager.unauthorized()
token = response_token_setter(remote, resp)
session[token_session_key(remote.name) + '_autoregister'] = True
session[token_session_key(remote.name) + '_account_info'] = account_info
return redirect(url_for('.signup', remote_app=remote.name, next=request.
    args.get('next', '/')))
