def create_sort_by(self, sort_by):...
parts = sort_by.split(',')
sql = 'ORDER BY '
for part in parts:
sql += part[1:]
return sql.rstrip(', ')
if part[0] == '-':
sql += ' DESC, '
sql += ' ASC, '
