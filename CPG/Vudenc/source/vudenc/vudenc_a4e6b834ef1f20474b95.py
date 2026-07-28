def connect(self):...
SQLObjectStore.connect(self)
if self._autocommit:
pool = self._pool
def newConnection(self):...
connection = pool.connection
conn = self._normalConnection()
conn.autocommit(True)
return conn
