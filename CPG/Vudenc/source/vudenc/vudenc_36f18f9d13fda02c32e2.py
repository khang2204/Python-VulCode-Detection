@blueprint.before_app_first_request...
"""docstring"""
user_logged_out.connect(oauth_logout_handler)
oauth.init_app(current_app)
for remote_app, conf in cfg['OAUTHCLIENT_REMOTE_APPS'].items():
if remote_app not in oauth.remote_apps:
remote = oauth.remote_app(remote_app, **conf['params'])
remote = oauth.remote_apps[remote_app]
remote.tokengetter(make_token_getter(remote))
handlers.register(remote_app, remote.authorized_handler(make_handler(conf.
    get('authorized_handler', authorized_default_handler), remote)))
disconnect_handlers.register(remote_app, make_handler(conf.get(
    'disconnect_handler', disconnect_handler), remote, with_response=False))
def dummy_handler(remote, *args, **kargs):...
signup_handler = conf.get('signup_handler', dict())
account_info_handler = make_handler(signup_handler.get('info',
    dummy_handler), remote, with_response=False)
account_setup_handler = make_handler(signup_handler.get('setup',
    dummy_handler), remote, with_response=False)
account_view_handler = make_handler(signup_handler.get('view',
    dummy_handler), remote, with_response=False)
signup_handlers.register(remote_app, dict(info=account_info_handler, setup=
    account_setup_handler, view=account_view_handler))
