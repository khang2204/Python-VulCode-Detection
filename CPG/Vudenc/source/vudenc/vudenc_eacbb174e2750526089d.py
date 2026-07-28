def option_isdefault(cursor, option):...
"""docstring"""
query = """
    SELECT boot_val,
           reset_val
    FROM pg_settings
    WHERE name = '%s'
    """
cursor.execute(query % option)
rows = cursor.fetchone()
if cursor.rowcount > 0:
default_value, current_value = rows[0], rows[1]
return False
return default_value == current_value
