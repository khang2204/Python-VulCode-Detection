def option_get_default_value(cursor, option):...
"""docstring"""
query = """
    SELECT boot_val
    FROM pg_settings
    WHERE name = '%s'
    """
cursor.execute(query % option)
return cursor.fetchone()[0]
