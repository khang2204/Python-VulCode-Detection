@app.route('/logout')...
user = current_user
user.authenticated = False
db.session.add(user)
db.session.commit()
logout_user()
return 'logged out'
