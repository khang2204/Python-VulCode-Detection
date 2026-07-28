from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from .serializer import make_row_serializable
from .cache import Cache
from .connection_url import is_sqlite
def __init__(self, keys, rows):...
self.has_rows = rows is not None
self.keys = keys
self.rows = rows
@classmethod...
if result.returns_rows:
keys = result.keys()
return cls(None, None)
rows = [make_row_serializable(row) for row in result]
return cls(keys, rows)
