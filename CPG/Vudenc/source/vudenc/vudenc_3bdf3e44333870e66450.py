def set_route_type(self, i, m, t):...
self.log.debug('Setting %s,%s type to %d', i, m, t)
def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Succesfully set route type for (%s, %s) to %s', i, m, wzrpc
    .name_route_type(t))
if status == wzrpc.status.e_req_denied:
return self.wz_wait_reply(accept, *self.wz.make_auth_set_route_type_data(i,
    m, t, wzauth_data.set_route_type[i, m]))
self.log.warn('Status {0}, reauthentificating'.format(wzrpc.name_status(
    status)))
self.log.warn('Status {0}, retrying'.format(wzrpc.name_status(status)))
self.auth_requests()
that.retry = True
