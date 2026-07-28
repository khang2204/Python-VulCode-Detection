def make_req_msg(self, interface, method, args, fun, reqid=None):...
if not reqid:
reqid = self.make_reqid()
msg = make_req_msg(interface, method, args, reqid)
self.set_response_handler(reqid, fun)
return msg
