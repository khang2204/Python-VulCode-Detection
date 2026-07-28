@app.route('/level-2/index')...
conn = psycopg2.connect('dbname=unlock user=ubuntu')
cur = conn.cursor()
cur.execute('SELECT * FROM nile_items;')
res = cur.fetchall()
cur.close()
conn.close()
items = [dict() for x in range(len(res))]
for i in range(len(res) - 1, -1, -1):
items[i]['name'] = res[i][0]
return render_template('level-2/index.html', items=items, count=len(items))
items[i]['price'] = res[i][1]
items[i]['image'] = res[i][2]
