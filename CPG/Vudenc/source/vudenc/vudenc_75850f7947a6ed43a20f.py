from __future__ import print_function
import os
import sys
import etcd
from custodia.store.interface import CSStore, CSStoreError, CSStoreExists
def log_error(error):...
print(error, file=sys.stderr)
def __init__(self, config):...
self.server = config.get('etcd_server', '127.0.0.1')
self.port = int(config.get('etcd_port', 4001))
self.namespace = config.get('namespace', '/custodia')
self.etcd = etcd.Client(self.server, self.port)
log_error('Error creating namespace %s: [%r]' % (self.namespace, repr(err)))
def get(self, key):...
self.etcd.write(self.namespace, None, dir=True)
result = self.etcd.get(os.path.join(self.namespace, key))
log_error('Error fetching key %s: [%r]' % (key, repr(err)))
return result.value
