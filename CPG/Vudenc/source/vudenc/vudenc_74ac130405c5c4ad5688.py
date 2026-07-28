@tornado.web.authenticated...
if enable_authentication:
print('User {} logging out'.format(self.current_user))
self.redirect('/')
if self.current_user in authenticated_users:
authenticated_users.remove(self.current_user)
self.redirect('/login')
