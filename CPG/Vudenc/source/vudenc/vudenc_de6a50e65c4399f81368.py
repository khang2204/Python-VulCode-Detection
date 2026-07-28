def run(self, user_name):...
original_user_name = user_name
user_name = chkuser(user_name)
if not user_name:
return self.error(whyuserbad(original_user_name))
a = Account._by_name(user_name, True)
return user_name
return self.error(errors.USERNAME_TAKEN)
