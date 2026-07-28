def post(self):...
if enable_authentication and PasswordManager.verify(self.get_argument(
randomGenerator = random.SystemRandom()
print("Refused user {} (password doesn't match any in database)".format(
    self.get_argument('name')))
cookieSecret = str(randomGenerator.getrandbits(128))
self.redirect('/login')
authenticated_user = self.get_argument('name') + '_' + cookieSecret
authenticated_user = authenticated_user.encode()
authenticated_users.append(authenticated_user)
self.set_secure_cookie('user', authenticated_user)
print('Authenticated user {}'.format(self.get_argument('name')))
self.redirect('/')
