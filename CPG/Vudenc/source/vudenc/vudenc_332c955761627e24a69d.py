def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Successfull auth for (%s, %s)', i, m)
if status == wzrpc.status.e_auth_wrong_hash:
if wzrpc.status.e_timeout:
self.log.warn('Timeout {0}, retrying'.format(data[0]))
self.log.warning('Recvd unknown reply for (%s, %s) %s: %s', i, m, wzrpc.
    name_status(status), repr(data))
that.retry = True
