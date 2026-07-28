def check(self):...
sid = self.get_secure_cookie('sid')
if not sid:
return False
email = self.session.get('email')
user = dbapi.User()
if email and user.get_user(email) == 0:
profile = user.get_user_all(email)
self.clear_cookies()
if profile:
return False
self.id = profile[0]
self.time = profile[4]
self.email = email
return True
