@staticmethod...
if cursor is None or query_set is None:
return dict()
fields = DBManager.get_fields(cursor)
return dict(zip(fields, list(query_set)))
