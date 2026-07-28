def chpasswd(self, username, password, crypt_id=6, salt_len=10):...
if self.is_sys_user(username):
passwd_hash = textutil.gen_password_hash(password, crypt_id, salt_len)
cmd = "echo '{0}'|pw usermod {1} -H 0 ".format(passwd_hash, username)
ret, output = shellutil.run_get_output(cmd, log_cmd=False)
if ret != 0:
