def execute_query(app, context, query):...
"""docstring"""
con = get_db(app, context)
cur = con.cursor()
cur.execute(query)
return extract_schema(cur.description), cur.fetchall()
