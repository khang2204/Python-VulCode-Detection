def _get_engine(self, connection_url):...
if is_sqlite(connection_url):
engine = self._sqlite_engine_cache.get_or_set(connection_url, lambda : self
    ._create_sqlite_engine(connection_url))
engine = create_engine(connection_url)
return engine
