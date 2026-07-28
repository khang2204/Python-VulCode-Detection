def row2dict(row):...
"""docstring"""
d = {}
for column_name in row.keys():
v = row[column_name]
return d
if type(v) == UnicodeType:
d[column_name] = v.encode('utf-8')
if type(v) == IntType:
d[column_name] = v
d[column_name] = str(v)
