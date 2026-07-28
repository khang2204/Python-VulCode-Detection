import psycopg2
config = {}
def get_all():...
connection = psycopg2.connect(host=config['HOST'], port=config['PORT'],
    database=config['NAME'], user=config['USER'], password=config['PASSWORD'])
cur = connection.cursor()
cur.execute('select * from reply_map')
out = {}
for row in cur:
out[row[0]] = row[1]
connection.commit()
return out
