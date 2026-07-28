def create_tables(pg_connection):...
conn = psycopg2.connect(dbname=pg_connection['database'], user=
    pg_connection['user'], password=pg_connection['password'], host=
    pg_connection['host'])
cur = conn.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS quests
    (id SERIAL PRIMARY KEY, tier VARCHAR, description VARCHAR, creator VARCHAR, completed BOOLEAN);
    """
    )
conn.commit()
cur.close()
conn.close()
