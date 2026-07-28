def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Succesfully set route type for (%s, %s) to %s', i, m, wzrpc
    .name_route_type(t))
if status == wzrpc.status.e_req_denied:
self.log.warn('Status {0}, reauthentificating'.format(wzrpc.name_status(
    status)))
self.log.warn('Status {0}, retrying'.format(wzrpc.name_status(status)))
self.auth_requests()
that.retry = True
