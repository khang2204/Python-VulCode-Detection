def auth_requests(self):...
for i, m in self.wz_auth_requests:
def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Successfull auth for (%s, %s)', i, m)
if status == wzrpc.status.e_auth_wrong_hash:
self.wz_wait_reply(accept, *self.wz.make_auth_req_data(i, m, wzauth_data.
    request[i, m]))
if wzrpc.status.e_timeout:
self.log.warn('Timeout {0}, retrying'.format(data[0]))
self.log.warning('Recvd unknown reply for (%s, %s) %s: %s', i, m, wzrpc.
    name_status(status), repr(data))
that.retry = True
