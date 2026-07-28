@auth.route('/confirm')...
token = current_user.generate_confirmation_token()
send_email(current_user.email, 'Confirm Your Account', 'auth/email/confirm',
    user=current_user, token=token)
flash('A new confirmation email has been sent.')
return redirect(url_for('main.index'))
