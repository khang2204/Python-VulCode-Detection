def make_auth_bind_route_data(self, interface, method, key, reqid=None):...
if not reqid:
reqid = self.make_reqid()
args = [interface, method, make_auth_hash(interface, method, reqid, key)]
return b'Router', b'auth-bind-route', args, reqid
