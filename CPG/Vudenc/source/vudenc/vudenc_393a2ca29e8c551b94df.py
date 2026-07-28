@auth.route('/register', methods=['GET', 'POST'])...
form = RegistrationForm()
if form.validate_on_submit():
user = User(email=form.email.data, username=form.username.data, password=
    form.password.data)
return render_template('auth/register.html', form=form)
db.session.add(user)
db.session.commit()
token = user.generate_confirmation_token()
send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=
    user, token=token)
flash('Check your inbox! A confirmation email has been sent.')
return redirect(url_for('auth.login'))
