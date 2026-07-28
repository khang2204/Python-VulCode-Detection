def get_current_user(self):...
"""docstring"""
session_key = self.get_secure_cookie('session_key')
if not session_key:
return None
login_session = Login_Session.get_by_key(session_key, self.sql_session)
if not login_session:
return None
return User.by_key(login_session.userkey, self.sql_session).scalar()
