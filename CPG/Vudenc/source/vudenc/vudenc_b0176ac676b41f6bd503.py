def make_auth_set_route_type_data(self, interface, method, type_, key,...
if not reqid:
reqid = self.make_reqid()
args = [interface, method, struct.pack('!B', type_), make_auth_hash(
    interface, method, reqid, key)]
return b'Router', b'auth-set-route-type', args, reqid
