def release_lock(self):...
"""docstring"""
if not self._lock.acquired:
return False
self._lock.release()
return True
