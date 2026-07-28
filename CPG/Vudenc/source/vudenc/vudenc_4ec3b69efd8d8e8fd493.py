def signup_handler(remote, *args, **kwargs):...
"""docstring"""
if current_user.is_authenticated():
return redirect('/')
oauth_token = token_getter(remote)
if not oauth_token:
return redirect('/')
if not session.get(token_session_key(remote.name) + '_autoregister', False):
return redirect(url_for('.login', remote_app=remote.name))
form = EmailSignUpForm(request.form)
if form.validate_on_submit():
account_info = session.get(token_session_key(remote.name) + '_account_info')
return render_template('oauthclient/signup.html', form=form, remote=remote,
    app_title=cfg['OAUTHCLIENT_REMOTE_APPS'][remote.name].get('title', ''),
    app_description=cfg['OAUTHCLIENT_REMOTE_APPS'][remote.name].get(
    'description', ''), app_icon=cfg['OAUTHCLIENT_REMOTE_APPS'][remote.name
    ].get('icon', None))
user = oauth_register(account_info, form.data)
if user is None:
session.pop(token_session_key(remote.name) + '_autoregister', None)
if not oauth_authenticate(remote.consumer_key, user, require_existing_link=
return current_app.login_manager.unauthorized()
token = token_setter(remote, oauth_token[0], secret=oauth_token[1])
handlers = signup_handlers[remote.name]
if token is None:
if not token.remote_account.extra_data:
handlers['setup'](token)
session.pop(token_session_key(remote.name) + '_account_info', None)
if request.args.get('next', None):
return redirect(request.args.get('next'))
return redirect('/')
