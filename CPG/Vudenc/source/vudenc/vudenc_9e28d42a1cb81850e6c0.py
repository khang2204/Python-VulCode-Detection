def check_session(session_id):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute('SELECT * FROM UserData WHERE session_id = ?', [session_id])
verified = cursor.fetchone()
connection.close()
return verified
