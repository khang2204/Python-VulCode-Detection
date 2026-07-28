def extend(self, key, value):...
if isinstance(value, list):
for v in value:
self.append(key, v)
