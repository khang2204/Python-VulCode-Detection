def __init__(self, columns):...
self.columns = Column.to_columns(columns)
self._lookup = {}
self._flattened = []
for column in self.columns:
self._flattened.extend(column.type.flatten(column.name))
for col in self._flattened:
if col.flattened in self._lookup:
self._lookup[col.flattened] = col
self._lookup[col.escaped] = col
