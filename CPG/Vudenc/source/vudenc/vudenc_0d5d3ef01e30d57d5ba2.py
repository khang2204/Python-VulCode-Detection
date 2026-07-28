@app.route('/register', methods=['GET', 'POST'])...
if request.method == 'POST':
hashedPassword = generate_password_hash(request.form['password'])
return render_template('user/register/registration.html')
status = reg.registerUser(request.form['email'], hashedPassword, mysql)
if status == 'Success':
return render_template('user/register/success.html')
return render_template('user/register/error.html', name=request.form['email'])
