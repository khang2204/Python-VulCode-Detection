def option_reset(cursor, option):...
"""docstring"""
if not option_isdefault(cursor, option):
query = "ALTER SYSTEM SET %s TO '%s'"
return False
cursor.execute(query % (option, option_get_default_value(cursor, option)))
return True
