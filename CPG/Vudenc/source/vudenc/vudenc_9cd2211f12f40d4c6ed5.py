def __getitem__(self, path):...
for context in reversed(self.contexts):
value = context.get(path, MISSING)
if value is not MISSING:
return value
