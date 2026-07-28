def add_filter(self, value, op='='):...
for regex, column in self.filter_map.items():
if re.search(regex, value):
m = re.search(regex, value)
v = m.group(1)
self.columns[column].filter(v, op)
