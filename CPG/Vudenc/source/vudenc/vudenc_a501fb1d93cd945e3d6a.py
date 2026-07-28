@query_cached...
if self._connection is None:
self._connection = self._engine.connect()
dataframe = pandas.read_sql(sql=sql, con=self._connection, params=bindings)
return dataframe
