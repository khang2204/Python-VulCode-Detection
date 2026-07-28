@app.route('/register', methods=['GET', 'POST'])...
form = RegisterForm(request.form)
if request.method == 'POST' and form.validate():
name = form.name.data
return render_template('register.html', form=form)
email = form.email.data
username = form.username.data
password = sha256_crypt.encrypt(str(form.password.data))
cur = mysql.connection.cursor()
cur.execute(
    'INSERT INTO Users(name, email, username, password) VALUES(%s, %s, %s, %s)'
    , (name, email, username, password))
mysql.connection.commit()
cur.close()
flash('You are now registered and can log in', 'success')
return redirect(url_for('login'))
