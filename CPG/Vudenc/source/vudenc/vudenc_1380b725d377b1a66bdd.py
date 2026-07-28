@app.route('/login', methods=['GET', 'POST'])...
if current_user.is_authenticated:
return redirect(url_for('view_home'))
login_form = LoginForm()
if login_form.validate_on_submit():
login_user(login_form.user, remember=True)
return render_template('login.html', form=login_form)
return redirect(url_for('view_home'))
