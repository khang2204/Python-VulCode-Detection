@app.route('/login', methods=['POST'])...
email = request.form['email']
password = request.form['password']
user = query_user(email)
if user != None:
if check_password_hash(user.password, password):
flash('Incorrect Email/Password')
session['email'] = email
return redirect('/login')
returnUrl = session.pop('return_url', None)
if returnUrl:
return redirect(returnUrl)
return redirect('/')
