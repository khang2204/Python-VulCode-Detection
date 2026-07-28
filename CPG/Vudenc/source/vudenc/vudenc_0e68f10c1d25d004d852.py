def __exit__(self, exc_type, exc_value, tb):...
if self._observe is None:
Device._current_context = None
self.execute()
