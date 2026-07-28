def get_all_old_sourcebyinstitutions(conn, sqlite):...
"""docstring"""
query = """
        SELECT
            sourcebyinstitution
        FROM
            sourcebyinstitution
        GROUP BY
            sourcebyinstitution
    """
sqlite.execute(query)
old_sourcebyinstitutions = []
for record in sqlite:
old_sourcebyinstitution = record[0]
return old_sourcebyinstitutions
old_sourcebyinstitutions.append(old_sourcebyinstitution)
