def __init__(self, orig_obj, lock):...
self.orig_obj = orig_obj
self.lock = lock
self._wrapper_cache = {}
