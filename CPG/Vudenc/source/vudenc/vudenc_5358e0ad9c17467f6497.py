def add_notes(secure_fname, file_id, username):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute(
    """INSERT INTO Notes(secure_name, user_id, uuid_filename)
                        VALUES (?, 
                        (SELECT user_id FROM UserData WHERE username = ?),
                         ?)"""
    , (secure_fname, username, file_id))
connection.commit()
connection.close()
