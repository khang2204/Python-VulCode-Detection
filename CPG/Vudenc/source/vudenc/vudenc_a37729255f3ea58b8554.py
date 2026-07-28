def useradd(self, username, expiration=None):...
"""docstring"""
userentry = self.get_userentry(username)
if userentry is not None:
logger.warn('User {0} already exists, skip useradd', username)
if expiration is not None:
return
cmd = 'pw useradd {0} -e {1} -m'.format(username, expiration)
cmd = 'pw useradd {0} -m'.format(username)
retcode, out = shellutil.run_get_output(cmd)
if retcode != 0:
