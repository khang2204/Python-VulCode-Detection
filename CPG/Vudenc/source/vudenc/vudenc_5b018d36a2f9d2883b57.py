def is_username_taken(username):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute('SELECT * FROM UserData WHERE username = ?', [username])
records = cursor.fetchone()
connection.close()
return records
