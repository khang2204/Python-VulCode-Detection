def __init__(self, config):...
self.server = config.get('etcd_server', '127.0.0.1')
self.port = int(config.get('etcd_port', 4001))
self.namespace = config.get('namespace', '/custodia')
self.etcd = etcd.Client(self.server, self.port)
log_error('Error creating namespace %s: [%r]' % (self.namespace, repr(err)))
self.etcd.write(self.namespace, None, dir=True)
