def option_matches(cursor, option, value):...
"""docstring"""
query = "SELECT current_setting('%s') = '%s'"
cursor.execute(query % (option, value))
return cursor.fetchone()[0]
