def passes_email_suffix(self, email):...
if self.allowed_email_suffix:
return email.endswith(self.allowed_email_suffix)
return True
