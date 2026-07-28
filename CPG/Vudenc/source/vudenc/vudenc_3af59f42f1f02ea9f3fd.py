def validate(self):...
rv = FlaskForm.validate(self)
if not rv:
return False
user = auth_get_user_by_email(self.email.data)
if user:
self.password.errors.append('Email already registered')
if len(self.password.data) < 8:
return False
self.password.errors.append('Password should be at least 8 characters long')
self.user = auth_add_user(self.email.data, self.password.data)
return False
return True
