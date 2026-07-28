def add_post(content):...
"""docstring"""
db = psycopg2.connect('dbname=forum')
c = db.cursor()
c.execute("INSERT INTO posts (content) VALUES ('%s')" % content)
db.commit()
db.close()
