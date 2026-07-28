def __setitem__(self, path, value):...
node, key = traverse(self, path, sep=self._sep, on_missing=self.
    _create_on_missing)
if node is self:
self._data[key] = value
node[key] = value
