@app.route('/level-1/inbox')...
conn = psycopg2.connect('dbname=unlock user=ubuntu')
cur = conn.cursor()
cur.execute('SELECT * FROM bmail_emails;')
res = cur.fetchall()
cur.close()
conn.close()
emails = [dict() for x in range(len(res))]
account = request.args.get('account')
for i in range(len(res) - 1, -1, -1):
if res[i][4] == account:
return render_template('level-1/inbox.html', account=account, emails=emails,
    count=len(emails))
emails[i]['title'] = res[i][0]
emails[i]['body'] = res[i][1]
emails[i]['sender'] = res[i][2]
emails[i]['tags'] = res[i][3]
