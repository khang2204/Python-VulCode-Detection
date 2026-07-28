def create_select(self, fields):...
if fields == '*':
return 'SELECT *'
sql = 'SELECT '
for field in fields:
sql += '{} AS {}, '.format(field, fields[field])
return sql.rstrip(', ')
