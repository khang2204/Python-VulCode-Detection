def get(self):...
if not self.current_user:
self.render('../login.html')
self.redirect('/')
return
