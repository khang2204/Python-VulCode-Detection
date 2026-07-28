def insert_items(self, index, items):...
self[index:index + 1] = items
add = len(items) - 1
for name, (i, j) in self._names.items():
if i > index:
self._names[name] = i + add, j + add
if i == index:
self.set_name(name, i, end=i + len(items))
