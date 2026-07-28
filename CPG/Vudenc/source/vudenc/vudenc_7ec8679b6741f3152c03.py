def post(self, command):...
if not users.is_current_user_admin():
self.response.set_status(403)
commands[command](self).post()
return
