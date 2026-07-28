@app.route('/login', methods=['GET', 'POST'])...
if request.method == 'POST':
user = User(request.form['email'], request.form['password'])
return render_template('login.html')
db.session.add(user)
db.session.commit()
return redirect(url_for('tables'))
