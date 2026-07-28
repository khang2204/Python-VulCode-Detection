def read_file(self, to_read):...
"""docstring"""
self.log_debug('Reading file %s' % to_read)
if err.errno == 2:
if not self.local:
self.log_debug('File %s does not exist on node' % to_read)
self.log_error('Error reading %s: %s' % (to_read, err))
remote = self.sftp.open(to_read)
return rfile.read()
return ''
return remote.read()
