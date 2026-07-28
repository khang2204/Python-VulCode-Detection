def confirm_owner_of_file(file_id, session_id, username):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute(
    """SELECT session_id, username FROM UserData WHERE user_id = 
                                (SELECT user_id FROM Notes WHERE uuid_filename = ?)"""
    , [file_id])
row = cursor.fetchone()
connection.close()
return row[0] == session_id and row[1] == username
