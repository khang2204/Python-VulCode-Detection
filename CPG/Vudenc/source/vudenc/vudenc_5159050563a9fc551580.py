@app.route('/auth/login', methods=['GET', 'POST'])...
if request.method == 'GET':
return render_login()
form = LoginForm(request.form)
if not form.validate():
return render_loginForm(form)
user = User.query.filter_by(username=form.username.data, password=form.
    password.data).first()
if not user:
return render_loginInvalid(form)
login_user(user)
return redirect(url_for('index'))
