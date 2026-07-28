@auth.route('/login', methods=['GET', 'POST'])...
form = LoginForm()
if form.validate_on_submit():
user = User.query.filter_by(email=form.email.data).first()
return render_template('auth/login.html', form=form)
if user is not None and user.verify_password(form.password.data):
login_user(user, form.remember_me.data)
flash('Invalid username or password.')
session['auth_token'] = user.auth_token
return redirect(request.args.get('next') or url_for('main.index'))
