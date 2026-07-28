def generate_add(self, query):...
table_name = query.model_class._meta.table_name
query = (
    "INSERT INTO {0} ({1}) SELECT {2} WHERE NOT EXISTS (SELECT {3} FROM {0} WHERE {3}='{5}' AND {4}='{6}');"
    .format(table_name, ','.join(query.model_class._meta.
    sorted_fields_names), ','.join([str(obj.id) for obj in query.objs]),
    query.model_class._meta.sorted_fields_names[0], query.model_class._meta
    .sorted_fields_names[1], query.objs[0].id, query.objs[1].id))
return query
