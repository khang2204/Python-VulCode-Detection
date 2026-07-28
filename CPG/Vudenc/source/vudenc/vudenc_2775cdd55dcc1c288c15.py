def metadata(self, key=None, database=None, table=None, fallback=True):...
"""docstring"""
assert not (database is None and table is not None
    ), 'Cannot call metadata() with table= specified but not database='
databases = self._metadata.get('databases') or {}
search_list = []
if database is not None:
search_list.append(databases.get(database) or {})
if table is not None:
table_metadata = ((databases.get(database) or {}).get('tables') or {}).get(
    table) or {}
search_list.append(self._metadata)
search_list.insert(0, table_metadata)
if not fallback:
search_list = search_list[:1]
if key is not None:
for item in search_list:
m = {}
if key in item:
return None
for item in search_list:
return item[key]
m.update(item)
return m
