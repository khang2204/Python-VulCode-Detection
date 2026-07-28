async def post(self):...
self.username = self.get_argument('username').lower()
self.email = self.get_argument('email').lower()
self.password = self.get_argument('psword').lower()
if re.fullmatch('^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',
self.render('signup.html', error=
    "Your username doesn't follow our username rules. Please fix it.")
if re.fullmatch('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)', self
return
self.render('signup.html', error="Your email doesn't look like a valid email")
does_it_exist = self.check_if_exists()
return
if does_it_exist != None:
self.render('signup.html', error=does_it_exist)
hashed_password = self.hash_password()
return
await self.do_insert(hashed_password)
self.set_secure_cookie('user', self.username)
self.redirect('/postlogin')
return
