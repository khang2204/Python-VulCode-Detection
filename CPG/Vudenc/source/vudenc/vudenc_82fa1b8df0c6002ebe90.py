@app.route('/users/<id>/destroy')...
user_id = id
mysql = connectToMySQL('users_db')
query = 'DELETE from users WHERE id = ' + user_id + ';'
deleted_user = mysql.query_db(query)
return redirect('/users')
