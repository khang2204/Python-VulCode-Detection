@app.route('/logout')...
session.clear()
flash('You are now logged out', 'success')
return redirect(url_for('login'))
