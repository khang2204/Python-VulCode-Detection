def del_account(self, username):...
if self.is_sys_user(username):
logger.error('{0} is a system user. Will not delete it.', username)
shellutil.run('> /var/run/utx.active')
shellutil.run('rmuser -y ' + username)
self.conf_sudoer(username, remove=True)
