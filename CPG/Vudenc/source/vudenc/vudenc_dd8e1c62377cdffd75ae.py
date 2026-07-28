def post(self):...
self.username = self.get_argument('username').lower()
self.password = self.get_argument('psword').lower()
check_details = self.check_database()
if check_details != None:
self.render('signin.html', error=check_details)
self.set_secure_cookie('user', self.username)
return
self.redirect('/postlogin')
return
