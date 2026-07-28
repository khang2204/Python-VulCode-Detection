def execute(query, params=None):...
conn = connect()
c = conn.cursor()
if not params:
c.execute(query)
c.execute(query, params)
conn.commit()
conn.close()
