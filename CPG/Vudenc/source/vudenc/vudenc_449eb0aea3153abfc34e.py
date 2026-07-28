def unload(self, sql=None, filename=None, **kwargs):...
cache = kwargs.pop('cache', False)
sql = self.__prepare(sql, filename)
return self._unload(sql, kwargs, cache=cache)
