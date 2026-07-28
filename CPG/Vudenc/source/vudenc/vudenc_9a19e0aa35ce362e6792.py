def get_sql(self, select, table, where, sort_by=None, offset=None, limit=None):...
sql = self.create_select(select) + ' '
sql += self.create_from(table) + ' '
sql += self.create_where(where)
if sort_by:
sql += ' ' + self.create_sort_by(sort_by)
if offset and limit:
sql += ' ' + self.create_offset(offset, limit)
return sql
