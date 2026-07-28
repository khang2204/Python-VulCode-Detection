@auth.route('/change-email', methods=['GET', 'POST'])...
form = ChangeEmailForm()
if form.validate_on_submit():
if current_user.verify_password(form.password.data):
return render_template('auth/change_email.html', form=form)
new_email = form.email.data
flash('Invalid password.')
token = current_user.generate_email_change_token(new_email)
send_email(new_email, 'Confirm Your Email Address',
    'auth/email/change_email', user=current_user, token=token)
flash(
    'An email with instructions for confirming your new email address has been sent.'
    )
return redirect(url_for('main.index'))
