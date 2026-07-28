def queryAll(query):...
"""docstring"""
conn = None
result = None
conn_string = (
    "host='localhost' dbname='data1000' user='postgres' password='postgres'")
print(error)
if conn is not None:
print('Connecting to the PostgreSQL database...')
conn.close()
return result
conn = psycopg2.connect(conn_string)
print('Database connection closed.')
cur = conn.cursor()
cur.execute(query)
result = cur.fetchall()
print(result)
cur.close()
