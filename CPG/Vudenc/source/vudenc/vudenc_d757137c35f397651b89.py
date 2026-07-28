def set_name(self, name, index, end=None):...
"""docstring"""
self._names[name] = index, end
if end is None:
setattr(self, name, self[index])
setattr(self, name, Namedlist(toclone=self[index:end]))
