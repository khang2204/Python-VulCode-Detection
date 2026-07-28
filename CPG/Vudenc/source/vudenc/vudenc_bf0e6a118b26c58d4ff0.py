def dataframe(self, sql=None, filename=None, **kwargs):...
cache = kwargs.pop('cache', False)
sql = self.__prepare(sql, filename)
dataframe = self._dataframe(sql, kwargs, cache=cache)
buffer = StringIO()
dataframe.info(buf=buffer, memory_usage='deep')
logger.info(buffer.getvalue())
logger.info(dataframe.head())
return dataframe
