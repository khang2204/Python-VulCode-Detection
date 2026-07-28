def __getitem__(self, path):...
node, key = traverse(self, path, sep=self._sep, on_missing=raise_on_missing)
if node is self:
return self._data[key]
return node[key]
