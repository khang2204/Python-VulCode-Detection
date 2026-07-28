@app.route('/login', methods=['POST'])...
user = User.query.get(request.form['email'])
if user:
if request.form['password'] == user.pwd:
return render_template('unsuccessful-login.html')
user.authenticated = True
db.session.add(user)
db.session.commit()
login_user(user, remember=True)
return redirect(url_prefix)
