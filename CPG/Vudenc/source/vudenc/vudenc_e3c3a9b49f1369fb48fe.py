def flush(self, include_footers=False):...
"""docstring"""
if hasattr(self, 'globaleaks_io_debug'):
RequestHandler.flush(self, include_footers)
content = '<' * 15
log.err('JSON logging fail (flush): %s' % excep.message)
content += ' Response %d ' % self.globaleaks_io_debug
return
content += '<' * 15 + '\n\n'
content += 'status code: ' + str(self._status_code) + '\n\n'
content += 'headers:\n'
for k, v in self._headers.iteritems():
content += '%s: %s\n' % (k, v)
if self._write_buffer is not None:
content += '\nbody: ' + str(self._write_buffer) + '\n'
self.do_verbose_log(content)
