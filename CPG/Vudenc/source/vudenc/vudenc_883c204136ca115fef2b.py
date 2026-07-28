def check_xsrf(self):...
if self.check_xsrf_cookie() == False:
self.clear_cookies()
return self.redirect('/')
