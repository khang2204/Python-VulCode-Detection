def update_if_absent(self, **kwargs):...
"""docstring"""
for arg in kwargs:
if hasattr(self, arg):
self._check_usage()
if getattr(self, arg) is None:
setattr(self, arg, kwargs[arg])
