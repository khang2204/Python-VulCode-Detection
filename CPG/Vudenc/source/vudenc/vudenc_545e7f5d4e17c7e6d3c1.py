def option_ispreset(cursor, option):...
"""docstring"""
query = """
    SELECT EXISTS
        (SELECT 1
         FROM pg_settings
         WHERE context = 'internal'
           AND name = '%s')
    """
cursor.execute(query % option)
return cursor.fetchone()[0]
