def clear_pool(self):...
logger.info('Closing the MySQL connection pool (id {})'.format(id(self)))
while not self._pool.empty():
db = self._pool.get()
logger.info('Closed all connections in the MySQL connection pool (id {})'.
    format(id(self)))
if not isinstance(db, MySQLdb.connections.Connection):
return 0
db.close()
self._pool.task_done()
