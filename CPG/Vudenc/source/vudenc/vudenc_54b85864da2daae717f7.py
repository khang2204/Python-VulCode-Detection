def get_posts():...
"""docstring"""
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('select content,time from posts order by time desc')
return c.fetchall()
