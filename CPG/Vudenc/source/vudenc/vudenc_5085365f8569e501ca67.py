def fetchone(query):...
conn = connect()
cur = conn.cursor()
cur.execute(query)
result = cur.fetchone()[0]
conn.close()
return result
