def get_connection(self):...
logger.debug('Retrieving connection from the pool')
db = self._pool.get()
logger.debug('Type checking connection')
if not isinstance(db, MySQLdb.connections.Connection):
return -1
logger.info('Successful MySQL connection get request')
return db
