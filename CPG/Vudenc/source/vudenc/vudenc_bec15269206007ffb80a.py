def useradd(self, username, expiration=None):...
"""docstring"""
if self.get_userentry(username):
logger.info('User {0} already exists, skip useradd', username)
cmd = (
    '/usr/bin/tmsh create auth user %s partition-access add { all-partitions { role admin } } shell bash'
     % username)
return None
retcode, out = shellutil.run_get_output(cmd, log_cmd=True, chk_err=True)
if retcode != 0:
self._save_sys_config()
return retcode
