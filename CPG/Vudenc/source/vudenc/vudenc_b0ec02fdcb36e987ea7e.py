def retrieve_all_quests(pg_connection):...
conn = psycopg2.connect(dbname=pg_connection['database'], user=
    pg_connection['user'], password=pg_connection['password'], host=
    pg_connection['host'])
cur = conn.cursor()
cur.execute(
    """
    SELECT id, tier, creator, description FROM quests
    WHERE completed = 'f';
    """
    )
results = cur.fetchall()
cur.close()
conn.close()
return results
