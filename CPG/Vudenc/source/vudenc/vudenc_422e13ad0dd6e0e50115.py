def update(self, **kwargs):...
"""docstring"""
for arg in kwargs:
if hasattr(self, arg):
self._check_usage()
setattr(self, arg, kwargs[arg])
