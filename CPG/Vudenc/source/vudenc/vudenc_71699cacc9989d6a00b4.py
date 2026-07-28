def post(self):...
self.check_xsrf()
email = self.get_arg('email')
email = email.strip()
password = self.get_arg('password')
password2 = self.get_arg('password2')
user = dbapi.User()
error = ''
if email and password == password2:
if user.get_user(email) == 0:
if password != password2:
error = 'user already exist'
result = user.insert_user(email, password)
error = 'password inconsistent'
error = 'missing argument'
return self.get(error)
if result != -1:
m = hashlib.md5()
error = 'insert falure, try again later'
m.update(email)
email_md5 = m.hexdigest()
self.session['email'] = email
self.session['email_md5'] = email_md5
self.set_secure_cookie('sid', self.session.session_id)
return self.redirect('/user')
