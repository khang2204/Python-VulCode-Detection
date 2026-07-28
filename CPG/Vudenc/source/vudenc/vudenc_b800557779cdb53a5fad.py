def get(self):...
cookie_status = self.get_secure_cookie('user')
if cookie_status == None:
self.render('index.html')
self.render('postlogin.html')
return
return
