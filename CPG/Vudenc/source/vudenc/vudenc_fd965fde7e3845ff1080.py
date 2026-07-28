def make_archive_readable(self, filepath):...
"""docstring"""
cmd = 'chmod o+r %s' % filepath
res = self.run_command(cmd, timeout=10, need_root=True)
if res['status'] == 0:
return True
msg = 'Exception while making %s readable. Return code was %s'
self.log_error(msg % (filepath, res['status']))
