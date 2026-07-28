def retrieve_quest_data(pg_connection, query):...
conn = psycopg2.connect(dbname=pg_connection['database'], user=
    pg_connection['user'], password=pg_connection['password'], host=
    pg_connection['host'])
cur = conn.cursor()
cur.execute(query)
results = list(cur.fetchall())
cur.close()
conn.close()
return results
