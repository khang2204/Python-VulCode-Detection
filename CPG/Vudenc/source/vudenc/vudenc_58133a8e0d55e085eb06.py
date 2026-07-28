def run(self, password, verify):...
if not chkpass(password):
return self.error()
if verify != password:
return self.error(errors.BAD_PASSWORD_MATCH)
return password
