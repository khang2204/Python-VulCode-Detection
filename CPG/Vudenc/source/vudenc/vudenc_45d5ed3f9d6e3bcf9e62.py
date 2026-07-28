def delete_quest(pg_connection, quest_id):...
conn = psycopg2.connect(dbname=pg_connection['database'], user=
    pg_connection['user'], password=pg_connection['password'], host=
    pg_connection['host'])
cur = conn.cursor()
cur.execute("""
    DELETE FROM quests
    WHERE id = %s;""", quest_id)
conn.commit()
cur.close()
conn.close()
