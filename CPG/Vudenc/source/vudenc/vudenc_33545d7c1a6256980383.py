def sosreport(self):...
"""docstring"""
self.finalize_sos_cmd()
self.log_debug('Final sos command set to %s' % self.sos_cmd)
path = self.execute_sos_command()
self.cleanup()
if path:
self.finalize_sos_path(path)
self.log_error('Unable to determine path of sos archive')
if self.sos_path:
self.retrieved = self.retrieve_sosreport()
