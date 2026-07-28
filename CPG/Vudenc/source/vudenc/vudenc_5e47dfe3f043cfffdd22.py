def get_secure_filename(file_id):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute('SELECT secure_name FROM Notes WHERE uuid_filename = ?', [
    file_id])
row = cursor.fetchone()
connection.close()
return row[0]
