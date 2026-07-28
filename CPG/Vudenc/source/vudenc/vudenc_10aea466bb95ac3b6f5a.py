@app.route('/users/<id>/edit', methods=['GET', 'POST'])...
user_id = id
mysql = connectToMySQL('users_db')
if request.method == 'POST':
query = (
    'UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email= %(e)s, description = %(d)s, updated_at = now() WHERE id = '
     + user_id + ';')
user = mysql.query_db('SELECT * FROM users WHERE id = ' + user_id + ';')
data = {'fn': request.form['first_name'], 'ln': request.form['last_name'],
    'e': request.form['email'], 'd': request.form['description']}
return render_template('edit.html', user=user[0])
mysql.query_db(query, data)
return redirect('/users/{}'.format(user_id))
