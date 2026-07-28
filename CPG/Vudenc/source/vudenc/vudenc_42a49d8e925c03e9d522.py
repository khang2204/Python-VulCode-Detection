@auth.route('/unconfirmed')...
if current_user.is_anonymous or current_user.confirmed:
return redirect(url_for('main.index'))
return render_template('auth/unconfirmed.html')
