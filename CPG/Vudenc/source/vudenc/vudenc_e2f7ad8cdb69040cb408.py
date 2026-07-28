import hashlib
from webapp.web import BaseHandler
from model import dbapi
def check_xsrf(self):...
if self.check_xsrf_cookie() == False:
error = 'xsrf invalid'
def get(self, error=''):...
self.get(error)
xsrf_token = self.xsrf_from_html()
params = {'error_info': error, 'xsrf_token': xsrf_token}
body = self.wrap_html('templates/register.html', params)
return self.write(body)
