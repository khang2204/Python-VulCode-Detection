def generate_update(self, query):...
if query.model_class._meta.primary_key:
_id = query.values['id']
keys = ','.join([x.encode('utf-8') for x in query.values.keys()])
values = ','.join([x.encode('utf-8') for x in query.values.values()])
if query.model_class._meta.primary_key:
str_query = 'UPDATE {0} SET ({1})=({2}) WHERE id = {3}'.format(query.
    model_class._meta.table_name, keys, values, _id)
print('ERROR: Not primary key cannot update row. Need to be implemented')
if query.return_id:
str_query += ' RETURNING id'
str_query += ';'
return str_query
