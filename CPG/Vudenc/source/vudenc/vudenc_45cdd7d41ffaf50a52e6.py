@auth.route('/confirm/<token>')...
if current_user.confirmed:
return redirect(url_for('main.index'))
if current_user.confirm(token):
flash('Your account is confirmed. Thank you!')
flash('The confirmation link is invalid or has expired.')
return redirect(url_for('main.index'))
