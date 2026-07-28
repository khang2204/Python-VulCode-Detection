def fetchall(query):...
conn = connect()
cur = conn.cursor()
cur.execute(query)
records = cur.fetchall()
conn.close()
return records
