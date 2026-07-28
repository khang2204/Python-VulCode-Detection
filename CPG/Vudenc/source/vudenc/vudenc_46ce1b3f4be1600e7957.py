def generate_delete(self, query):...
where = ''
if query._where:
i = 0
query = 'DELETE FROM {0} {1};'.format(query.model_class._meta.table_name, where
    )
if isinstance(query._where, str):
return query
where = 'WHERE {0}'.format(query._where)
for value in query._where:
if i == 0:
con = 'WHERE '
con = ' AND '
where += "%s %s.%s %s '%s'" % (con, value.lhs.model_class._meta.table_name,
    value.lhs.name, value.op, value.rhs)
i += 1
