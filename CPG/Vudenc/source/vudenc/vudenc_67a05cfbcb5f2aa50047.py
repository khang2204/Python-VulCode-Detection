def set_field_tables(self):...
"""docstring"""
if len(self.tables) > 1:
for i, f in enumerate(self.fields):
if '.' not in f:
self.fields[i] = '{0}.{1}'.format(self.tables[0], f)
