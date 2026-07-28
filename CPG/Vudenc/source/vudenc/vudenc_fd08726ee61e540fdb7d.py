def update(query):...
conn = psycopg2.connect('dbname=fluffy_bot user=censored password=Laumau11p')
cur = conn.cursor()
cur.execute(query)
conn.commit()
cur.close()
conn.close()
