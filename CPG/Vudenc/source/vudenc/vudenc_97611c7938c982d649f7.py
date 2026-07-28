""" Client blueprint used to handle OAuth callbacks. """
from __future__ import absolute_import
from flask import Blueprint, abort, current_app, url_for, request
from flask.ext.login import user_logged_out
from invenio.base.globals import cfg
from invenio.ext.sslify import ssl_required
from ..client import oauth, handlers, disconnect_handlers, signup_handlers
from ..handlers import authorized_default_handler, make_token_getter, make_handler, disconnect_handler, oauth_logout_handler
blueprint = Blueprint('oauthclient', __name__, url_prefix='/oauth',
    static_folder='../static', template_folder='../templates')
@blueprint.before_app_first_request...
"""docstring"""
user_logged_out.connect(oauth_logout_handler)
oauth.init_app(current_app)
for remote_app, conf in cfg['OAUTHCLIENT_REMOTE_APPS'].items():
if remote_app not in oauth.remote_apps:
@blueprint.route('/login/<remote_app>/')...
remote = oauth.remote_app(remote_app, **conf['params'])
remote = oauth.remote_apps[remote_app]
"""docstring"""
remote.tokengetter(make_token_getter(remote))
if remote_app not in oauth.remote_apps:
handlers.register(remote_app, remote.authorized_handler(make_handler(conf.
    get('authorized_handler', authorized_default_handler), remote)))
return abort(404)
callback_url = url_for('.authorized', remote_app=remote_app, next=request.
    args.get('next') or request.referrer or None, _external=True)
disconnect_handlers.register(remote_app, make_handler(conf.get(
    'disconnect_handler', disconnect_handler), remote, with_response=False))
return oauth.remote_apps[remote_app].authorize(callback=callback_url)
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
