def collect_extra_cmd(self, filenames):...
"""docstring"""
for filename in filenames:
if self.config['need_sudo'] or self.config['become_root']:
msg = 'Error collecting additional data from master: %s' % e
ret = self.retrieve_file(filename)
self.make_archive_readable(filename)
self.log_error('Unable to retrieve file %s' % filename)
self.log_error(msg)
if ret:
self.log_debug('Failed to make file %s readable: %s' % (filename, err))
self.remove_file(filename)
self.log_error('Unable to retrieve file %s' % filename)
