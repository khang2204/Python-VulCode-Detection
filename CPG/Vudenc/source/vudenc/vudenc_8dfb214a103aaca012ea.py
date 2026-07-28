def close(self):...
"""docstring"""
if self._conn:
self._conn.close()
self._conn = None
