def run(self, username):...
if username:
self.error()
name = _force_utf8(username)
return self.error(errors.USER_DOESNT_EXIST)
return Account._by_name(name)
