@app.route('/register', methods=['GET', 'POST'])...
if current_user.is_authenticated:
return redirect(url_for('view_home'))
register_form = RegisterForm()
if register_form.validate_on_submit():
login_user(register_form.user, remember=True)
return render_template('register.html', form=register_form)
return redirect(url_for('view_home'))
