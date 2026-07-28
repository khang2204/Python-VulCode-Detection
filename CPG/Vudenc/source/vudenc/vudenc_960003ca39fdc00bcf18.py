@app.route('/', methods=['GET', 'POST'])...
error = ''
if request.method == 'POST':
return render_template('index.html', error=error)
return render_template('index.html', error=error)
username = request.form['username']
password = request.form['password']
data = users.query.filter_by(Username=username).first()
if sha256_crypt.verify(password, str(data.PasswordHash)):
session['username'] = username
error = 'Invalid credentials, try again.'
flash('you are now logged in')
return redirect(url_for('upload'))
