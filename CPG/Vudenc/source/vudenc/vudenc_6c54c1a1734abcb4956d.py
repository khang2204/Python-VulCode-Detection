def connect(self):...
"""docstring"""
if socket.gethostname() == config.PROD_HOST_NAME:
log.info('Connecting to the local database...')
log.info('Connecting to the database via SSH...')
port = 3306
if not self.tunnel_opened:
self.conn = MySQLdb.connect(host='127.0.0.1', user=config.DB_USER, password
    =config.DB_PASSWD, port=port, database=config.DB_NAME, charset='utf8')
self._open_ssh_tunnel()
port = self.tunnel.local_bind_port
log.info('Connected to the database.')
