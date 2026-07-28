def passes_email_whitelist(self, email):...
if self.allowed_email_whitelist is not None:
return email in self.allowed_email_whitelist
return True
