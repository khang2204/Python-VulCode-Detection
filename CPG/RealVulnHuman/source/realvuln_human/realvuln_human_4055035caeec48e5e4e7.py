with get_db_connection() as conn:
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    current_user = cursor.fetchone()

# Get form data
new_username = request.form['username'] or current_user['username']
email = request.form['email'] or current_user['email']
country = request.form['country'] or current_user['country']
if 'role' not in request.form:
    role = current_user['role']
else:
    role = request.form['role'] or current_user['role']
#role = request.form['role'] or current_user['role']
#permissions = request.form['permissions'] or current_user['permissions']
if 'permissions' not in request.form:
    permissions = current_user['permissions']
else:
    permissions = request.form['permissions']
team = request.form['team'] or current_user['team']

# Handle profile picture upload
profile_picture_id = current_user['profile_picture']
if 'profile_picture' in request.files:
    file = request.files['profile_picture']
    if file:
        # Generate simple incremental ID for profile picture
        # Get the highest existing ID and increment it by 1
        cursor.execute("SELECT MAX(profile_picture) FROM users")
