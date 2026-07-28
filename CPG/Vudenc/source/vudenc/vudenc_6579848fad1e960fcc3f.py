@auth.route('/logout')...
logout_user()
flash('You have logged out.')
return redirect(url_for('main.index'))
