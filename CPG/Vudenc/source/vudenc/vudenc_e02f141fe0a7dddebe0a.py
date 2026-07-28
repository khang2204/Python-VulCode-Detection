def _run_ssh(self, cmd_list, attempts=1):...
utils.check_ssh_injection(cmd_list)
command = ' '.join(cmd_list)
if not self.sshpool:
password = self.configuration.san_password
total_attempts = attempts
LOG.error(_('Error running SSH command: %s') % command)
privatekey = self.configuration.san_private_key
while attempts > 0:
min_size = self.configuration.ssh_min_pool_conn
attempts -= 1
msg = _(
    "SSH Command failed after '%(total_attempts)r' attempts : '%(command)s'"
    ) % {'total_attempts': total_attempts, 'command': command}
max_size = self.configuration.ssh_max_pool_conn
LOG.info(_('EQL-driver: executing "%s"') % command)
LOG.exception(e)
self.sshpool = utils.SSHPool(self.configuration.san_ip, self.configuration.
    san_ssh_port, self.configuration.ssh_conn_timeout, self.configuration.
    san_login, password=password, privatekey=privatekey, min_size=min_size,
    max_size=max_size)
return self._ssh_execute(ssh, command, timeout=self.configuration.
    eqlx_cli_timeout)
greenthread.sleep(random.randint(20, 500) / 100.0)
