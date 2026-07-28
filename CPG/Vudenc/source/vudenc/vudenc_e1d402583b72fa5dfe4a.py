def generic_search(keywords, tables, app, context):...
result = []
for table in tables:
query = 'SELECT * FROM {} WHERE 1=0'.format(table)
return result
description = execute_query(app, context, query)[0]
conditions = []
for col in description:
conditions.append("{} LIKE '%{}%'".format(col, keywords))
conditions = ' OR '.join(conditions)
query = 'SELECT * FROM {} WHERE {}'.format(table, conditions)
schema, data = execute_query(app, context, query)
result.append((table, schema, data))
