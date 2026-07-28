@app.route('/auth/register/', methods=['POST'])...
form = RegisterForm(request.form)
if not form.validate():
return render_registerForm(form)
u = User(form.username.data, form.password.data)
db.session().add(u)
db.session.commit()
login_user(u)
return redirect(url_for('index'))
