"""
if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return render_template('login.html', error='Please provide username and password')

    # Query the database for the user using parameterized query
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ? OR email = ?"
        cursor.execute(query, (username,username))
        user = cursor.fetchone()

    # Check if the user exists and the password matches
    if user and user['password'] == custom_hash(password):
        session['username'] = user['username']
        session['user_id'] = user['id']

        # Update last_login timestamp
        cursor.execute("UPDATE users SET last_login = ? WHERE username = ?", (datetime.datetime.now(), username))
        conn.commit()
