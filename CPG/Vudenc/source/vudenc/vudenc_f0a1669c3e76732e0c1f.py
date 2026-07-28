def post(self):...
if self.check() == False:
return self.redirect('/')
self.check_xsrf()
oldpassword = self.get_arg('oldpassword')
password = self.get_arg('password')
password2 = self.get_arg('password2')
user = dbapi.User()
error = ''
if password == password2 and user.check_user(self.email, oldpassword) != -1:
result = user.update_password(self.email, password)
if password != password2:
if result != -1:
error = 'new password inconsistent'
error = 'old password incorrect'
error = 'Update Password Successfully'
error = 'Update failure, try again later'
return self.get(error)
