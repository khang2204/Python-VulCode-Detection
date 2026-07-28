def make_proxy(self, accessor, relationship_direction, options=None):...
"""docstring"""
if options is None:
options = {}
return self.proxy_class(self._data, accessor, relationship_direction, **options
    )
