def check_xsrf(self):...
if self.check_xsrf_cookie() == False:
error = 'xsrf invalid'
self.get(error)
