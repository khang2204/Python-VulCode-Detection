def build_filter_string(self):...
s = 'WHERE '
l = []
for c in self.columns.values():
if c.filter_string:
if len(l) > 0:
l.append(c.filter_string)
return s + ' AND '.join(l)
return ''
