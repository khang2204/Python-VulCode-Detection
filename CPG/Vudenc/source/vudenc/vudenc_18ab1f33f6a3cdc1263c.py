def close():...
"""docstring"""
if _pool is not None:
_pool.close()
_pool = None
