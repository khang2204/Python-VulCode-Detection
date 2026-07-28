def span(self, key):...
path = os.path.join(self.namespace, key)
self.etcd.write(path, None, dir=True, prevExist=False)
log_error('Error storing key %s: [%r]' % (key, repr(err)))
