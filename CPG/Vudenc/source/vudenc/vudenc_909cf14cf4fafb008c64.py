def __execute(self, sql, bindings):...
if self._connection is None:
self._connection = self._engine.connect()
return self._connection.execute(sql, bindings)
