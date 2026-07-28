def get_hostname(self):...
"""docstring"""
sout = self.run_command('hostname')
self.hostname = sout['stdout'].strip()
self.log_debug('Hostname set to %s' % self.hostname)
