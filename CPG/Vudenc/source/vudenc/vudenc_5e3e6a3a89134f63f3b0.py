@handler.post(handler.JSON, handler.JSON)...
"""docstring"""
id_token = self.request.get('idToken')
expires_in = datetime.timedelta(days=SESSION_EXPIRY_DAYS)
session_cookie = auth.create_session_cookie(id_token, expires_in)
expires = datetime.datetime.now() + expires_in
self.response.set_cookie('session', session_cookie, expires=expires,
    httponly=True, secure=True, overwrite=True)
self.render_json({'status': 'success'})
