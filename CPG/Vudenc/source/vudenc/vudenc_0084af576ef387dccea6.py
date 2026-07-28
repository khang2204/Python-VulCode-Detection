@app.route('/login', methods=['GET', 'POST'])...
if current_user.is_authenticated:
return redirect('/manage')
form = LoginForm()
if form.validate_on_submit():
user = User.query.filter_by(username=form.username.data).first()
return render_template('login.html', title='Sign In', form=form)
if user is None or not user.check_password(form.password.data):
flash('Invalid username or password')
login_user(user, remember=form.remember_me.data)
return redirect('/login')
next_page = request.args.get('next')
if not next_page or url_parse(next_page).netloc != '':
next_page = '/manage'
return redirect(next_page)
