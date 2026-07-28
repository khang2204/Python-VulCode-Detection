def __init__(self, name, columns, filter_func, display_name):...
"""docstring"""
self.name = name
self.columns = columns
self.type = columns[0].type
self.column_selects = []
for c in columns:
self.column_selects.append(c.select())
self.filter_string = None
self.filter_func = filter_func
self.display_name = display_name
