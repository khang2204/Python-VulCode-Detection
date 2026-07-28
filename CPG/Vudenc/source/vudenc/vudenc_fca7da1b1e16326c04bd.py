@app.route('/flag-check/<level>', methods=['POST'])...
conn = psycopg2.connect('dbname=unlock user=ubuntu')
cur = conn.cursor()
cur.execute('SELECT * FROM unlock_flags WHERE level=' + level + ';')
res = cur.fetchone()
cur.close()
conn.close()
if str(request.form['flag']) == str(res[1]):
if int(current_user.level1_progress) <= 2:
return 'false'
current_user.level1_progress = 3
if int(current_user.progress) <= 1:
current_user.progress = 2
db.session.commit()
return 'true'
