with get_db_connection() as conn:
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? OR email = ?"
    cursor.execute(query, (username, username))
    user = cursor.fetchone()

if user and user['password'] == custom_hash(password):

    # Generate JWT
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Token expires in 24 hours
    }, Config.SECRET_KEY, algorithm='HS256')


    # Update last_login timestamp
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET last_login = ? WHERE username = ?", (datetime.datetime.now(), username))
        conn.commit()

    return {'message': 'Login successful', 'token': token}, 200
else:
