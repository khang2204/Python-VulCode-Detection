def option_set(cursor, option, value):...
"""docstring"""
if not option_matches(cursor, option, value):
query = "ALTER SYSTEM SET %s TO '%s'"
return False
cursor.execute(query % (option, value))
return True
