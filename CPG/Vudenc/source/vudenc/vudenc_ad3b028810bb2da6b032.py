@staticmethod...
if cursor is None or query_set is None:
return list()
fields = DBManager.get_fields(cursor)
results = list(query_set)
return [dict(zip(fields, result)) for result in results]
return error_handle('Columns are not macthed')
