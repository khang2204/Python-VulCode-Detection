@app.route('/login', methods=['GET', 'POST'])...
form = loginForm(request.form)
if request.method == 'POST' and form.validate():
conn = mysql.connection
return render_template('login.html', form=form)
cur = conn.cursor()
cur.execute('SELECT id, password FROM users WHERE username="%s" ' % str(
    form.username.data))
rv = cur.fetchall()
if sha256_crypt.verify(form.password.data, str(rv[0]['password'])):
user = User(rv[0]['id'])
return 'Wrong password'
user.authenticate(form.username.data)
login_user(user)
flash('Logged in successfully.')
next = request.args.get('next')
if not is_safe_url(next):
return abort(400)
return redirect(next or url_for('home'))
