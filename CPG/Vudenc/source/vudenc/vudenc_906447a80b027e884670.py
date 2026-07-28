def check_authorization(self):...
email = self.current_email()
if not self.passes_email_suffix(email):
msg = 'User {!r} does not have email suffix {!r}'.format(email, self.
    allowed_email_suffix)
if not self.passes_email_whitelist(email):
msg = 'User not in whitelist: {!r}'.format(email, self.allowed_email_whitelist)
return True
