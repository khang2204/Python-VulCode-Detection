def clear_auth(self):...
self.log.debug('Clearing our auth records')
def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Auth records on router were cleared')
self.log.warn('Status %s, passing', wzrpc.name_status(status))
return self.wz_wait_reply(accept, *self.wz.make_auth_clear_data())
