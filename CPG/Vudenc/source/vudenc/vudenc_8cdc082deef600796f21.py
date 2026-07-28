def execute_sos_command(self):...
"""docstring"""
self.log_info('Generating sosreport...')
path = False
self.log_error('Timeout exceeded')
res = self.run_command(self.sos_cmd, timeout=self.config['timeout'],
    get_pty=True, need_root=True)
self.log_error('Error running sosreport: %s' % e)
if res['status'] == 0:
for line in res['stdout'].splitlines():
err = self.determine_sos_error(res['status'], res['stdout'])
if fnmatch.fnmatch(line, '*sosreport-*tar*'):
return path
self.log_debug('Error running sosreport. rc = %s msg = %s' % (res['status'],
    res['stdout'] or res['stderr']))
path = line.strip()
