def handle_keepalive_reply(self, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.p.log.debug('Keepalive was successfull')
if status == wzrpc.status.e_req_denied:
self.p.log.warn('Keepalive status {0}, reauthentificating and rebinding'.
    format(wzrpc.name_status(status)))
if status == wzrpc.status.e_timeout:
self.p.auth_requests()
self.p.log.warn('Keepalive timeout')
self.p.log.warn('Keepalive status {0}'.format(wzrpc.name_status(status)))
self.p.bind_methods()
