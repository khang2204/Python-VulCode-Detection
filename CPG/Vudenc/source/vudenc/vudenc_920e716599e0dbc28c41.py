def open_ssh_session(self):...
"""docstring"""
self.client = paramiko.SSHClient()
if not self.config['password']:
self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
self.log_error('Authentication failed. SSH keys installed?')
self.log_error('Authentication failed. Incorrect password.')
self.client.load_system_host_keys()
self.log_error(
    'Bad authentication type. The node rejected the authentication attempt.')
self.log_debug('Opening session to %s.' % self.address)
self.log_error(
    'Provided key was rejected by remote SSH client. Check ~/.ssh/known_hosts.'
    )
self.client.connect(self.address, username=self.config['ssh_user'], port=
    self.config['ssh_port'], password=self.config['password'] or None,
    timeout=15)
if err.errno == -2:
self.log_debug('%s successfully connected' % self._hostname)
self.log_error('Provided hostname did not resolve.')
self.log_error('Socket error trying to connect: %s' % err)
return True
msg = 'Unable to connect: %s' % err
if hasattr(err, 'errors'):
msg = self._determine_ssh_error(err.errors)
self.log_error(msg)
