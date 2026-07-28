@property...
if not self._metadata:
self._metadata = sqlalchemy.MetaData(bind=self._engine)
return self._metadata
