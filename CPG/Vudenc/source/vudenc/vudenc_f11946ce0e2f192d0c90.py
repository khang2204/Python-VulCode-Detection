def import_quest_data(pg_connection, quest_tier, quest_desc, creator):...
conn = psycopg2.connect(dbname=pg_connection['database'], user=
    pg_connection['user'], password=pg_connection['password'], host=
    pg_connection['host'])
cur = conn.cursor()
cur.execute(
    """
    INSERT INTO quests (tier, description, creator, completed)
    VALUES (%s, %s, %s, False);
    """
    , (quest_tier, quest_desc, creator))
conn.commit()
cur.close()
conn.close()
