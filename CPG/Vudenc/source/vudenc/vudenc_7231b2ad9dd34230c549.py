def set_params(self, **kwargs):...
"""docstring"""
self.set_defaults(**kwargs)
for k, v in kwargs.items():
self.overridable[k] = v
