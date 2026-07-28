# Weak encryption of password (DO NOT USE IN PRODUCTION)
hashed_password = custom_hash(password)

try:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "INSERT INTO users (username, email, country, password) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (username, email, country, hashed_password))
        conn.commit()
except Exception as e:
    print("Error inserting user:", e)  # Print the error message for debugging
    return render_template('signup.html', error='User already exists or database error')

query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
user = cursor.fetchone()

session['username'] = user['username']
session['user_id'] = user['id']

# Update last_login timestamp
