def accept(that, reqid, seqnum, status, data):...
if status == wzrpc.status.success:
self.log.debug('Route unbinded for (%s, %s)', i, m)
self.log.warn('Status %s, passing', wzrpc.name_status(status))
