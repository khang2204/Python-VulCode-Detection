def __getattr__(self, attr):...
orig_attr = getattr(self.orig_obj, attr)
if not callable(orig_attr):
return orig_attr
wrapper = self._wrapper_cache.get(attr)
if wrapper is None:
@functools.wraps(orig_attr)...
return wrapper
return orig_attr(*args, **kwargs)
