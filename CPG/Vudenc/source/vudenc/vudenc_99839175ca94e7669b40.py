def set(self, key, value, replace=False):...
path = os.path.join(self.namespace, key)
self.etcd.write(path, value, prevExist=replace)
log_error('Error storing key %s: [%r]' % (key, repr(err)))
