def dump_session_cookie(self, session_id):...
"""docstring"""
return dump_cookie(self.app.config.get('SESSION_COOKIE_NAME'), session_id,
    max_age=float(self.app.config.get('PERMANENT_SESSION_LIFETIME')), path=
    self.app.config.get('SESSION_COOKIE_PATH'), domain=self.app.config.get(
    'SESSION_COOKIE_DOMAIN'))
