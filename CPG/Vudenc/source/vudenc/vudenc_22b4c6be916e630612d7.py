@app.route('/users/<id>')...
mysql = connectToMySQL('users_db')
user = mysql.query_db('SELECT * FROM users WHERE id = {};'.format(id))
return render_template('user.html', user=user[0])
