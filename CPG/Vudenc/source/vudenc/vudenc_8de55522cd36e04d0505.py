@auth.route('/reset/<token>', methods=['GET', 'POST'])...
if not current_user.is_anonymous:
return redirect(url_for('main.index'))
form = PasswordResetForm()
if form.validate_on_submit():
user = User.query.filter_by(email=form.email.data).first()
return render_template('auth/reset_password.html', form=form)
if user is None:
return redirect(url_for('main.index'))
if user.reset_password(token, form.password.data):
flash('Your password has been updated.')
return redirect(url_for('main.index'))
return redirect(url_for('auth.login'))
