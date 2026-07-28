@property...
"""docstring"""
if self._inputsize is None:
self._inputsize = sum(f.size for f in self.input)
return self._inputsize
