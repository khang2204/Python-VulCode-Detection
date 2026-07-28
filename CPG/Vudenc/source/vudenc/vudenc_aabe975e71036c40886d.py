@app.route('/users')...
mysql = connectToMySQL('users_db')
users = mysql.query_db('SELECT * FROM users;')
return render_template('index.html', users=users)
