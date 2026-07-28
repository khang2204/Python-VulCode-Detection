"""
data = request.get_json()  # Get data from request body
username = data.get('username')
password = data.get('password')

if not username or not password:
    return {'error': 'Please provide username and password'}, 400

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
