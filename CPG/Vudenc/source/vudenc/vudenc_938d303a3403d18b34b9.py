def determine_host(self):...
"""docstring"""
for host_type in self.config['host_types']:
host = self.config['host_types'][host_type](self.address)
self.log_error('Unable to determine host installation. Ignoring node')
rel_string = self.read_file(host.release_file).strip()
rel_string = rel_string.decode('utf-8')
if host._check_enabled(rel_string):
self.log_debug('Host installation found to be %s' % host.distribution)
return host
