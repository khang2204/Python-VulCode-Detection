def clear(self) ->'Report':...
"""docstring"""
self.body = []
self.data = SharedCache()
self.files = SharedCache()
self._last_update_time = time.time()
return self
