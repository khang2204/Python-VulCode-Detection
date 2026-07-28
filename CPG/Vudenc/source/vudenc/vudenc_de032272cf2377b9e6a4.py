def add_post(content):...
"""docstring"""
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("insert into posts values('%s')" % content)
db.commit()
db.close()
