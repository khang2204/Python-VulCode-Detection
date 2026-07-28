def finalize_sos_path(self, path):...
"""docstring"""
pstrip = self.host.sos_path_strip
if pstrip:
path = path.replace(pstrip, '')
path = path.split()[0]
self.log_debug('Final sos path: %s' % path)
self.sos_path = path
self.archive = path.split('/')[-1]
