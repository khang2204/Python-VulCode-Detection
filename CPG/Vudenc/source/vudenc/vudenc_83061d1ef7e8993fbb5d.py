def option_exists(cursor, option):...
"""docstring"""
query = """
    SELECT name
    FROM pg_settings
    WHERE name = '%s'
    """
cursor.execute(query % option)
return cursor.rowcount > 0
