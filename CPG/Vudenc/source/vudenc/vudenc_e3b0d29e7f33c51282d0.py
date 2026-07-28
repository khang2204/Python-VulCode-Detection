def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Auth records on router were cleared')
self.log.warn('Status %s, passing', wzrpc.name_status(status))
