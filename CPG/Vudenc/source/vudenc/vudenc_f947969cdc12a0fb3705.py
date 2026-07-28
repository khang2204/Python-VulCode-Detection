def select(self, sql=None, filename=None, **kwargs):...
cache = kwargs.pop('cache', False)
sql = self.__prepare(sql, filename)
return self._select(sql, kwargs, cache=cache)
