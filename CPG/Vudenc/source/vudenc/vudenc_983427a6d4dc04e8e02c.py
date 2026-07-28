def run(self, name):...
user = VExistingUname.run(self, name)
if not user or not hasattr(user, 'email') or not user.email:
return self.error(errors.NO_EMAIL_FOR_USER)
return user
