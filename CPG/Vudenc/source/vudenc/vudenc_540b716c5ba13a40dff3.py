import os
import hashlib
import imghdr
from webapp.web import BaseHandler
from model import dbapi
MAX_FILE_SIZE = 5000000
def check_xsrf(self):...
if self.check_xsrf_cookie() == False:
return self.redirect('ftypeerror')
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
def get_filesize(self, file):...
self.time = profile[4]
file.seek(0, 2)
self.email = email
size = file.tell()
return True
file.seek(0)
return size
