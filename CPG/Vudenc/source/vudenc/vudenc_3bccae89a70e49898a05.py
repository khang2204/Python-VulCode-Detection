def allitems(self):...
next = 0
for name, index in sorted(self._names.items(), key=lambda item: item[1][0]):
start, end = index
for item in self[next:]:
if end is None:
yield None, item
end = start + 1
if start > next:
for item in self[next:start]:
yield name, getattr(self, name)
yield None, item
next = end
