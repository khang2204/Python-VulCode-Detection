def complete_quest(pg_connection, quest_id, completion):...
conn = psycopg2.connect(dbname=pg_connection['database'], user=
    pg_connection['user'], password=pg_connection['password'], host=
    pg_connection['host'])
cur = conn.cursor()
cur.execute(
    """
    UPDATE quests
    SET completed = '%s'
    WHERE id = %s;
    """,
    (completion, quest_id))
conn.commit()
cur.close()
conn.close()
