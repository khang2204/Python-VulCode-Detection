"""Login page."""
import datetime
from config import local_config
from handlers import base_handler
from libs import auth
from libs import handler
from libs import helpers
from metrics import logs
SESSION_EXPIRY_DAYS = 14
"""Login page."""
@handler.unsupported_on_local_server...
"""docstring"""
self.render('login.html', {'apiKey': local_config.ProjectConfig().get(
    'firebase.api_key'), 'authDomain': auth.auth_domain(), 'dest': self.
    request.get('dest')})
"""Session login handler."""
@handler.post(handler.JSON, handler.JSON)...
"""docstring"""
id_token = self.request.get('idToken')
expires_in = datetime.timedelta(days=SESSION_EXPIRY_DAYS)
session_cookie = auth.create_session_cookie(id_token, expires_in)
expires = datetime.datetime.now() + expires_in
self.response.set_cookie('session', session_cookie, expires=expires,
    httponly=True, secure=True, overwrite=True)
self.render_json({'status': 'success'})
"""Log out handler."""
@handler.unsupported_on_local_server...
"""docstring"""
auth.revoke_session_cookie(auth.get_session_cookie())
logs.log_error('Failed to revoke session cookie.')
self.response.delete_cookie('session')
self.redirect(self.request.get('dest'))
