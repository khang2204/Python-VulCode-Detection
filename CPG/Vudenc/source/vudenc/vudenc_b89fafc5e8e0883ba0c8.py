def add_post(content):...
"""docstring"""
conn = psycopg2.connect('dbname=forum')
cursor = conn.cursor()
cursor.execute("insert into posts values ('%s')" % content)
conn.commit()
conn.close()
