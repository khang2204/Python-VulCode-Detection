@app.route('/get-hint/<level>', methods=['POST'])...
conn = psycopg2.connect('dbname=unlock user=ubuntu')
cur = conn.cursor()
if int(level) == 1:
cur.execute('SELECT hint FROM unlock_hints WHERE level=1 AND progress=' +
    str(current_user.level1_progress) + ' AND difficulty=' + str(
    current_user.difficulty) + ';')
if int(level) == 2:
res = cur.fetchone()
cur.execute('SELECT hint FROM unlock_hints WHERE level=2 AND progress=' +
    str(current_user.level2_progress) + ' AND difficulty=' + str(
    current_user.difficulty) + ';')
if int(level) == 3:
cur.close()
res = cur.fetchone()
cur.execute('SELECT hint FROM unlock_hints WHERE level=3 AND progress=' +
    str(current_user.level3_progress) + ' AND difficulty=' + str(
    current_user.difficulty) + ';')
if int(level) == 4:
conn.close()
res = cur.fetchone()
cur.execute('SELECT hint FROM unlock_hints WHERE level=4 AND progress=' +
    str(current_user.level4_progress) + ' AND difficulty=' + str(
    current_user.difficulty) + ';')
return str(res[0])
res = cur.fetchone()
