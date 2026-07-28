def send_request(self, command, **args):...
if self.closed:
wait = args.pop('wait', False)
req = self._create_request(command, **args)
if self.VERBOSE:
msg = parse_message(req)
if wait:
print(' <-', msg)
self._conn.send(req)
resp_awaiter = self._get_awaiter_for_request(req, **args)
resp_awaiter = AwaitableResponse(req, lambda : resp['msg'])
self._conn.send(req)
return resp_awaiter
