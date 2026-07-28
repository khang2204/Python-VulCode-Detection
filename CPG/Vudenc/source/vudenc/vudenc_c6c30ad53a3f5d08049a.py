def get_posts():...
"""docstring"""
conn = psycopg2.connect('dbname=forum')
cursor = conn.cursor()
cursor.execute('select content, time from posts order by time desc')
all_posts = cursor.fetchall()
conn.close()
return all_posts
