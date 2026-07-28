def AddPost(content):...
conn = psycopg2.connect('dbname=forum')
cur = conn.cursor()
cur.execute("INSERT INTO posts (content) VALUES ('%s')" % content)
conn.commit()
conn.close()
