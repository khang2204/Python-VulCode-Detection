@app.route('/logout')...
if current_user.is_authenticated:
logout_user()
return redirect('/index')
return redirect('/index')
