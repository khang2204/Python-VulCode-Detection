@app.route('/login', methods=['GET', 'POST'])...
if request.method == 'POST':
username = request.form['username']
return render_template('login.html')
password_candidate = request.form['password']
cur = mysql.connection.cursor()
result = cur.execute('SELECT * FROM Users WHERE username = %s', [username])
if result > 0:
data = cur.fetchone()
error = 'Username not found'
password = data['password']
return render_template('login.html', error=error)
if sha256_crypt.verify(password_candidate, password):
session['logged_in'] = True
error = 'Invalid login'
session['username'] = username
return render_template('login.html', error=error)
flash('You are now logged in', 'success')
return redirect(url_for('index'))
