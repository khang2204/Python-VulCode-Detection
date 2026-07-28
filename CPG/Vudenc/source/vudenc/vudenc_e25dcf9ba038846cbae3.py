@auth.route('/reset', methods=['GET', 'POST'])...
if not current_user.is_anonymous:
return redirect(url_for('main.index'))
form = PasswordResetRequestForm()
if form.validate_on_submit():
user = User.query.filter_by(email=form.email.data).first()
return render_template('auth/reset_password.html', form=form)
if user:
token = user.generate_reset_token()
flash('An email with instructions for resetting your password has been sent.')
send_email(user.email, 'Reset Your Password', 'auth/email/reset_password',
    user=user, token=token, next=request.args.get('next'))
return redirect(url_for('auth.login'))
