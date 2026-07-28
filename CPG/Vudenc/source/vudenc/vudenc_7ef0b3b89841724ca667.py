def __init__(self, url, **kwargs):...
for int_value in ['pool_size', 'pool_recycle', 'max_overflow']:
if int_value in kwargs:
if 'poolclass' in kwargs:
kwargs[int_value] = int(kwargs[int_value])
kwargs['poolclass'] = getattr(sqlalchemy.pool, kwargs['poolclass'])
if '__name__' in kwargs:
self._engine = sqlalchemy.create_engine(url, **kwargs)
self._connection = None
self._metadata = None
self._transactions = []
