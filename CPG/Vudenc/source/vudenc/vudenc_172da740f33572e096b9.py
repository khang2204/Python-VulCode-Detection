def validate(self):...
rv = FlaskForm.validate(self)
if not rv:
return False
user = auth_get_user_by_email(self.email.data)
if not user or not auth_check_password(user, self.password.data):
self.password.errors.append('Invalid email or password')
self.user = user
return False
return True
