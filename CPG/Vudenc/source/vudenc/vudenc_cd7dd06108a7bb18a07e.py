def make_queries(table_name, field_names, values):...
queries = {'create': 'CREATE TABLE {} ({})'.format(table_name, field_names)}
queries.update({'insert':
    'INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'.
    format(table_name)})
return queries
