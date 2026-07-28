"""
Module that provides a way to connect to MySQL and reconnect each time
connection is lost. It also can automatically set up SSH tunnel thanks to
sshtunnel module

Original way to do it was described at
https://help.pythonanywhere.com/pages/ManagingDatabaseConnections/
"""
import socket
import MySQLdb
import sshtunnel
from photogpsbot import log
import config
"""
    Class that provides method to execute queries and handles connection to
    the MySQL database directly and via ssh if necessary
    """
conn = None
tunnel = None
tunnel_opened = False
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
def execute_query(self, query, parameters=None, trials=0):...
"""docstring"""
if not self.conn or not self.conn.open:
self.connect()
cursor = self.conn.cursor()
if e.args[0] in [2006, 2013]:
return cursor
cursor.execute(query, parameters)
log.info(e)
log.error(e)
def add(self, query):...
self.connect()
log.error(e)
"""docstring"""
if trials > 3:
self.execute_query(query)
log.errror(e)
def disconnect(self):...
log.error(e)
trials += 1
self.conn.commit()
"""docstring"""
log.warning('Ran out of limit of trials...')
log.warning(e)
if self.conn:
log.info('Trying execute the query again...')
self.conn.close()
if self.tunnel:
return self.execute_query(query, parameters, trials)
log.info('Connection to the database has been closed.')
self.tunnel.stop()
self.tunnel_opened = False
log.info('SSH tunnel has been closed.')
return True
