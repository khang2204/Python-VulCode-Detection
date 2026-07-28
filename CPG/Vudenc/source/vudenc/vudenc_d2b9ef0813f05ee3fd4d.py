def generate_remove(self, query):...
table_name = query.model_class._meta.table_name
query = "DELETE FROM {0} WHERE {1} = '{3}' AND {2}='{4}';".format(table_name,
    query.model_class._meta.sorted_fields_names[0], query.model_class._meta
    .sorted_fields_names[1], query.objs[0].id, query.objs[1].id)
return query
