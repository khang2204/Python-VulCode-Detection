def unbind_route(self, i, m):...
if not (i, m) in self.wz.req_handlers:
self.log.debug('Route %s,%s was not bound', i, m)
self.log.debug('Unbinding route %s,%s', i, m)
return
self.wz.del_req_handler(i, m)
def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Route unbinded for (%s, %s)', i, m)
self.log.warn('Status %s, passing', wzrpc.name_status(status))
return self.wz_wait_reply(accept, *self.wz.make_auth_unbind_route_data(i, m,
    wzauth_data.bind_route[i, m]))
