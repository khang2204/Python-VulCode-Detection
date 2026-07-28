def GetAllPosts():...
conn = psycopg2.connect('dbname=forum')
cur = conn.cursor()
cur.execute('SELECT time, content FROM posts ORDER BY time desc')
posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cur.
    fetchall())
conn.close()
return posts
