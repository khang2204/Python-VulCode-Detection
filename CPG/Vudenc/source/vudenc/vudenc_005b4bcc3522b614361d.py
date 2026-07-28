def parse(self, path):...
"""docstring"""
self._path = b(path, self.charset)
self._parts = None
self._leading_slash = False
self._trailing_slash = False
return self
