def decompress(self, value):...
if value is None:
return None
data = []
for i, field in enumerate(self.scheme['fields']):
fname, label, size = field
if '_legacy' in value and not data[-1]:
data.append(value.get(fname, ''))
data[-1] = value.get('_legacy', '')
return data
