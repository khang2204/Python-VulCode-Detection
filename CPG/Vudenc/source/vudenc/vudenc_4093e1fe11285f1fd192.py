def get_user_id(self):...
user = self.get_user()
if user:
user_id = user.user_id
user_id = None
return user_id
