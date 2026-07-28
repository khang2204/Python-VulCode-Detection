@app.route('/', methods=['POST'])...
print('login')
user = str(request.form['username'])
password = str(request.form['password'])
cur.execute("SELECT * FROM users WHERE name = '{}' AND password = '{}';".
    format(user, password))
response = cur.fetchone()
if response != None:
print(response, 'OK')
print(response, 'not OK')
return redirect(url_for('enter_test_point'))
flash('Invalid login or password')
return render_template('login.html')
