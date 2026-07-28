def make_auth_clear_data(self, reqid=None):...
if not reqid:
reqid = self.make_reqid()
return b'Router', b'auth-clear', [], reqid
