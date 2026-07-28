def retrieve_sosreport(self):...
"""docstring"""
if self.sos_path:
if self.config['need_sudo'] or self.config['become_root']:
if self.stderr.read():
self.logger.info('Retrieving sosreport from %s' % self.address)
self.make_archive_readable(self.sos_path)
self.log_error('Failed to make archive readable')
self.make_archive_readable(self.sos_path + '.md5')
self.log_debug('Failed to make md5 readable')
e = self.stderr.read()
e = [x.strip() for x in self.stdout.readlines() if x.strip][-1]
self.log_info('Retrieving sosreport...')
return False
self.logger.error('Failed to run sosreport on %s: %s' % (self.address, e))
ret = self.retrieve_file(self.sos_path)
self.log_error('Failed to run sosreport. %s' % e)
if ret:
return False
self.log_info('Successfully collected sosreport')
self.log_error('Failed to retrieve sosreport')
self.hash_retrieved = self.retrieve_file(self.sos_path + '.md5')
return False
return True
