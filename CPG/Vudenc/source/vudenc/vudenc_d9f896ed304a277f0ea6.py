@app.route('/level-2/search', methods=['POST'])...
term = str(request.form['term'])
conn = psycopg2.connect('dbname=unlock user=ubuntu')
cur = conn.cursor()
cur.execute('SELECT * FROM nile_items;')
res = cur.fetchall()
cur.close()
conn.close()
items = [dict() for x in range(len(res))]
for i in range(len(res) - 1, -1, -1):
if term in res[i][0] or term in res[i][3]:
return str(items)
items[i]['name'] = res[i][0]
items[i]['price'] = res[i][1]
items[i]['image'] = res[i][2]
