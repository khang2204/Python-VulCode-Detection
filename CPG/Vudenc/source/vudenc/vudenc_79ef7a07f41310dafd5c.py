def is_authenticated(self):...
"""docstring"""
if self.r_handler.current_user is not None:
self._check_xsrf_cookie()
token = self.r_handler.request.headers.get('Token', None)
return True
email = self.r_handler.request.headers.get('Email', None)
if token is not None and email is not None:
return False
user = self.session.query(SurveyCreator.token, SurveyCreator.token_expiration
    ).join(Email).filter(Email.address == email).one()
return False
if user.token_expiration.timetuple() < localtime():
return False
token_exists = user.token is not None
return token_exists and bcrypt_sha256.verify(token, user.token)
