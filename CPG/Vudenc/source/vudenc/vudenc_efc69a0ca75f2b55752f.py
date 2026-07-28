from webapp.web import BaseHandler
from model import dbapi
def check_xsrf(self):...
if self.check_xsrf_cookie() == False:
self.clear_cookies()
def check(self):...
return self.redirect('/')
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
self.time = profile[4]
def get(self, error=''):...
self.email = email
self.check()
return True
params = {'error_info': error, 'name': self.email, 'xsrf_token': self.
    xsrf_from_html()}
body = self.wrap_html('templates/pwdchange.html', params)
return self.write(body)
