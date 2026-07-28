def __enter__(self):...
if self._connection is None:
self._connection = self._engine.connect()
self._transactions.append(self._connection.begin())
return self
