def disconnect(self):...
"""docstring"""
if self.conn:
self.conn.close()
if self.tunnel:
log.info('Connection to the database has been closed.')
self.tunnel.stop()
self.tunnel_opened = False
log.info('SSH tunnel has been closed.')
return True
