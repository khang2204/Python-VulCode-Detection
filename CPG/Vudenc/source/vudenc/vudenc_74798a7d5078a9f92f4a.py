def _unique(form, field):...
sub = subtable and subname
query = 'SELECT COALESCE(COUNT(' + table + '.' + name + '), 0) FROM ' + table
if sub:
query += ' LEFT JOIN ' + subtable
query += ' WHERE (' + table + '.' + name + ' = :x'
if sub:
query += ' AND ' + subtable + '.id = ' + str(form[subname].data)
query += ');'
stmt = text(query)
res = db.engine.execute(stmt, x=field.data)
for row in res:
if row[0] > 0:
