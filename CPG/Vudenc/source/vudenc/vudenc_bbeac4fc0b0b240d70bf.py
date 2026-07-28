def make_router_req_msg(self, iden, interface, method, args, fun, reqid=None):...
msg = iden[:]
msg.append(b'')
msg.extend(self.make_req_msg(interface, method, args, fun, reqid))
return msg
