def __add__(self, other):...
if isinstance(other, TraversalPath):
return TraversalPath(*(self._path + other._path))
if isinstance(other, six.string_types):
return TraversalPath(*(self._path + tuple([(NotSupplied, NotSupplied, other)]))
    )
