def get(self):...
user = self.current_user
ret = {'user': None, 'email': None}
if user:
ret = {'user': user.name, 'email': user.email}
self.finish(ret)
