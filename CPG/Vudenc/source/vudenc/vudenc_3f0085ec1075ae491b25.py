@app.route('/signup', methods=['POST'])...
email = request.form['email']
user = query_user(email)
if user == None:
password = request.form['password']
flash('Email already in use')
password_hash = generate_password_hash(password)
return redirect('/signup')
insert_user(email, password_hash)
session['email'] = email
returnUrl = session.pop('return_url', None)
if returnUrl:
return redirect(returnUrl)
return redirect('/')
