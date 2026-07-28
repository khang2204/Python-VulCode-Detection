def extract_tables(self):...
"""docstring"""
self.tables = ['`tab' + self.doctype + '`']
if self.fields:
for f in self.fields:
if not ('tab' in f and '.' in f) or 'locate(' in f or 'count(' in f:
table_name = f.split('.')[0]
if table_name.lower().startswith('group_concat('):
table_name = table_name[13:]
if table_name.lower().startswith('ifnull('):
table_name = table_name[7:]
if not table_name[0] == '`':
table_name = '`' + table_name + '`'
if not table_name in self.tables:
self.append_table(table_name)
