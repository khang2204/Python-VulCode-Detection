def is_note_uuid_taken(uuid):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute('SELECT * FROM Notes WHERE uuid_filename = ?', [uuid])
records = cursor.fetchone()
connection.close()
return records
