@app.route('/register', methods=['GET', 'POST'])...
form = registerForm(request.form)
if request.method == 'POST' and form.validate():
conn = mysql.connection
return render_template('register.html', form=form)
cur = conn.cursor()
username = form.username.data
first_name = form.firstname.data
last_name = form.lastname.data
email = form.email.data
password = sha256_crypt.hash(form.password.data)
rv = cur.execute(
    'INSERT INTO users (first_name, last_name, username, password, email) VALUES (%s, %s, %s, %s, %s)'
    , (first_name, last_name, username, password, email))
conn.commit()
if str(rv):
return redirect(url_for('login'))
