def _open_ssh_tunnel(self):...
"""docstring"""
log.debug(
    'Establishing SSH tunnel to the server where the database is located...')
sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0
self.tunnel = sshtunnel.SSHTunnelForwarder(ssh_address_or_host=config.
    SERVER_ADDRESS, ssh_username=config.SSH_USER, ssh_password=config.
    SSH_PASSWD, ssh_port=22, remote_bind_address=('127.0.0.1', 3306))
self.tunnel.start()
self.tunnel_opened = True
log.debug('SSH tunnel has been established.')
