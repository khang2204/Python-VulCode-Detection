def run(self, user_name, password):...
user_name = chkuser(user_name)
user = None
if user_name:
user = valid_login(user_name, password)
if not user:
return self.error()
return user
