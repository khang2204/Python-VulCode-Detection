@app.route('/users/new', methods=['GET', 'POST'])...
if request.method == 'POST':
mysql = connectToMySQL('users_db')
return render_template('edit.html', user=None)
query = (
    'INSERT INTO users (first_name, last_name, email, description, created_at) VALUES (%(fn)s, %(ln)s, %(e)s, %(d)s, now());'
    )
data = {'fn': request.form['first_name'], 'ln': request.form['last_name'],
    'e': request.form['email'], 'd': request.form['description']}
new_user = mysql.query_db(query, data)
return redirect(f'/users/{new_user}')
