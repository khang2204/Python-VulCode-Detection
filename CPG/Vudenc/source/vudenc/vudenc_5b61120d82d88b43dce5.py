@auth.route('/change-email/<token>')...
if current_user.change_email(token):
session['auth_token'] = current_user.auth_token
flash('Invalid request.')
flash('Your email address has been updated.')
return redirect(url_for('main.index'))
