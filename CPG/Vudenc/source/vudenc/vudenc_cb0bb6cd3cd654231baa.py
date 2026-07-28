@app.route('/create-account', methods=['POST'])...
pwd = request.form['password']
email = request.form['email']
difficulty = request.form['difficulty']
user = User(email=email, pwd=pwd, difficulty=difficulty)
db_user = User.query.get(email)
if db_user:
return render_template('login.html', success=False)
user.authenticated = True
db.session.add(user)
db.session.commit()
login_user(user, remember=True)
return redirect(url_prefix)
