def chpasswd(self, username, password, crypt_id=6, salt_len=10):...
"""docstring"""
cmd = "/usr/bin/tmsh modify auth user {0} password '{1}'".format(username,
    password)
ret, output = shellutil.run_get_output(cmd, log_cmd=False, chk_err=True)
if ret != 0:
userentry = self.get_userentry('admin')
if userentry is None:
cmd = "/usr/bin/tmsh modify auth user 'admin' password '{0}'".format(password)
ret, output = shellutil.run_get_output(cmd, log_cmd=False, chk_err=True)
if ret != 0:
self._save_sys_config()
return ret
