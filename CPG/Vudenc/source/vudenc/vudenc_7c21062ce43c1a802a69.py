@app.route('/')...
if not session.get('logged_in'):
return redirect(url_for('users.login'))
user_id = session['logged_id']
sql = 'SELECT * FROM message where user_id = %d ORDER BY c_time DESC' % user_id
cursor.execute(sql)
m = cursor.fetchall()
messages = list(m)
for i, message in enumerate(messages):
message = list(message)
return render_template('show_entries.html', entries=messages)
user_id = message[1]
sql = 'SELECT nickname FROM users where user_id = %d' % user_id
cursor.execute(sql)
u = cursor.fetchone()
message.append(u[0])
sql = 'SELECT * FROM like_msg where msg_id = %d AND user_id = %d' % (message
    [0], user_id)
cursor.execute(sql)
like = cursor.fetchone()
if like is not None:
like_flag = 1
like_flag = 0
message.append(like_flag)
messages[i] = message
