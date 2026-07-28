def get(self, command):...
if not users.get_current_user():
self.redirect(users.create_login_url(self.request.url))
if not users.is_current_user_admin():
return
self.response.set_status(403)
commands[command](self).get()
return
