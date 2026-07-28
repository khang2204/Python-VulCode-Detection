def logout(session_id):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute('UPDATE UserData SET session_id = NULL WHERE session_id = ?',
    [session_id])
connection.commit()
connection.close()
