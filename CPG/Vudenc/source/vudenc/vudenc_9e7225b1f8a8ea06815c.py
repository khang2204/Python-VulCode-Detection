def put_connection(self, connection):...
logger.debug('Type checking connection')
if not isinstance(connection, MySQLdb.connections.Connection):
return -1
self._pool.put_nowait(connection)
self._pool.task_done()
logger.info('Successful MySQL connection put request')
return 0
