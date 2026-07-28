@handler.unsupported_on_local_server...
"""docstring"""
auth.revoke_session_cookie(auth.get_session_cookie())
logs.log_error('Failed to revoke session cookie.')
self.response.delete_cookie('session')
self.redirect(self.request.get('dest'))
