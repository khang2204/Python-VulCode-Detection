def get_all_old_institutions(conn, sqlite):...
"""docstring"""
query = """
        SELECT
            institution
        FROM
            institution
        GROUP BY
            institution
    """
sqlite.execute(query)
old_institutions = []
for record in sqlite:
old_institution = record[0]
return old_institutions
old_institutions.append(old_institution)
