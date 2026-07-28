def merge(self, path):...
"""docstring"""
if u(path).startswith('/'):
return self.parse(path)
if not self.trailing_slash and self.parts:
self.parts.pop()
path = self.new(path)
self.parts += path.parts
self._trailing_slash = path._trailing_slash
return self
