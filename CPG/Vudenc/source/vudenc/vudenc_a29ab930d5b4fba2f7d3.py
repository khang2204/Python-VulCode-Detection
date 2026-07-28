def get_data(cur, query):...
"""docstring"""
cur.execute(query)
cur.connection.rollback()
return cur.fetchall()
return None
