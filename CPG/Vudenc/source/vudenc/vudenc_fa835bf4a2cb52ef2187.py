def __init__(self, dbname, user, password, host, port=5432):...
self.db_conn = psycopg2.connect(host=host, dbname=dbname, user=user,
    password=password, port=port)
self.cursor = self.db_conn.cursor()
