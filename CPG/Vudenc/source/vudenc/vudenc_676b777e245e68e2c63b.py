def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.wz.set_req_handler(i, m, f)
if status == wzrpc.status.e_req_denied:
self.log.debug('Succesfully binded route (%s, %s)', i, m)
self.log.warn('Status {0}, reauthentificating'.format(wzrpc.name_status(
    status)))
if wzrpc.status.e_timeout:
self.auth_requests()
self.log.warn('Timeout {0}, retrying'.format(data[0]))
self.log.warn('Status {0}, retrying'.format(wzrpc.name_status(status)))
that.retry = True
that.retry = True
