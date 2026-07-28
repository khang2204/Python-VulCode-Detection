def generate_insert(self, query):...
keys = ','.join([x.encode('utf-8') for x in query.values.keys()])
values = ','.join([x.encode('utf-8') for x in query.values.values()])
str_query = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(query.model_class.
    _meta.table_name, keys, values)
if query.on_conflict:
str_query += ' ON CONFLICT ({0}) DO UPDATE SET ({1}) = ({2})'.format(','.
    join(query.on_conflict), keys, values)
if query.return_id:
str_query += ' RETURNING id'
str_query += ';'
return str_query
