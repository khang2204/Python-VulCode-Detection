@auth.route('/change-password', methods=['GET', 'POST'])...
form = ChangePasswordForm()
if form.validate_on_submit():
if current_user.verify_password(form.old_password.data):
return render_template('auth/change_password.html', form=form)
current_user.password = form.password.data
flash('Invalid password.')
db.session.add(current_user)
session['auth_token'] = current_user.auth_token
flash('Your password has been updated.')
return redirect(url_for('main.index'))
