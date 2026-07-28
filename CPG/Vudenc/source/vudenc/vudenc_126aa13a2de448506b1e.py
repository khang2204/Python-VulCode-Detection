def __enter__(self):...
if Device._current_context is None:
Device._current_context = self
return self
self.reset()
