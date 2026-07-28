import datetime
import psycopg2
def get_posts():...
db = psycopg2.connect('dbname=forum')
c = db.cursor()
"""Return all posts from the 'database', most recent first."""
c.execute('SELECT time, content FROM posts order by time DESC')
posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
db.close()
return posts
