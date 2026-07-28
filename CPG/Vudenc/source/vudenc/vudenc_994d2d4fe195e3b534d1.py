def newConnection(self):...
conn = self._normalConnection()
conn.autocommit(True)
return conn
