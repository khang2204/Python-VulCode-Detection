def run(self, password=None):...
if not c.user_is_loggedin:
if password is not None and not valid_password(c.user, password):
c.errors.add(errors.WRONG_PASSWORD)
