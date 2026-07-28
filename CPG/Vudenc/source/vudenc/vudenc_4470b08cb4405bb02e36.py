def get_all_old_sources(conn, sqlite):...
"""docstring"""
query = """
        SELECT
            source
        FROM
            source
        GROUP BY
            source
    """
sqlite.execute(query)
old_sources = []
for record in sqlite:
old_source = record[0]
return old_sources
old_sources.append(old_source)
