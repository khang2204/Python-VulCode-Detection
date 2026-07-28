@app.route('/login', methods=['GET', 'POST'])...
if request.method == 'POST':
response = usr.validateCredentials(request.form['username'], request.form[
    'password'], mysql)
return render_template('user/login.html')
if response:
name = request.form['username']
return render_template('user/login-error.html')
password = request.form['password']
cursor = mysql.connect().cursor()
cursor.execute('SELECT userId from Users WHERE userEmail="{0}";'.format(name))
idNum = cursor.fetchall()
cursor = mysql.connect().cursor()
cursor.execute('SELECT name from Calendars WHERE userId="{0}";'.format(idNum))
calendars = cursor.fetchall()
session['username'] = name
session['password'] = password
return redirect(url_for('dashboard', calendars=calendars))
