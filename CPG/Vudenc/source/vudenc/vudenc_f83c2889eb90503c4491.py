def insert(self, table, dataframe, batch_size=None):...
if batch_size is None:
batch_size = len(dataframe)
if self._connection is None:
self._connection = self._engine.connect()
dataframe.to_sql(table, self._connection, if_exists='append', index=False,
    chunksize=batch_size)
