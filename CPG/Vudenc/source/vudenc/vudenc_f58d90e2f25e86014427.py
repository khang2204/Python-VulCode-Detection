import psycopg2
user_table = 'user_objects'
rank_permit_table = 'rank_privileges'
def fetch(query):...
conn = psycopg2.connect('dbname=fluffy_bot user=censored password=Laumau11p')
cur = conn.cursor()
cur.execute(query)
result = cur.fetchall()
cur.close()
conn.close()
return result
