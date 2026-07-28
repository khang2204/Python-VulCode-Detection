def _run_ssh(self, command, check_exit_code=True, attempts=1):...
if not self.sshpool:
password = self.configuration.san_password
last_exception = None
privatekey = self.configuration.san_private_key
total_attempts = attempts
LOG.error(_('Error running SSH command: %s') % command)
min_size = self.configuration.ssh_min_pool_conn
while attempts > 0:
max_size = self.configuration.ssh_max_pool_conn
attempts -= 1
self.sshpool = utils.SSHPool(self.configuration.san_ip, self.configuration.
    san_ssh_port, self.configuration.ssh_conn_timeout, self.configuration.
    san_login, password=password, privatekey=privatekey, min_size=min_size,
    max_size=max_size)
return utils.ssh_execute(ssh, command, check_exit_code=check_exit_code)
LOG.error(e)
last_exception = e
greenthread.sleep(random.randint(20, 500) / 100.0)
