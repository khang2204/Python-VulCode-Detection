@classmethod...
if result.returns_rows:
keys = result.keys()
return cls(None, None)
rows = [make_row_serializable(row) for row in result]
return cls(keys, rows)
