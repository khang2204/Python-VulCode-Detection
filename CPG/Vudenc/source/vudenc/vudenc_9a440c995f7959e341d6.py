def login(username, password):...
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute(
    'SELECT user_id, password_hash, salt FROM UserData WHERE username = ?',
    [username])
data = cursor.fetchone()
if not data:
return None
user_id = data[0]
password_hash = data[1]
salt = data[2]
session_id = None
if multiple_hash_password(password, salt) == password_hash:
session_id = str(uuid.uuid4())
connection.close()
cursor.execute('UPDATE UserData SET session_id = ? WHERE user_id = ?', (
    session_id, user_id))
return session_id, notes
print('SID: ' + session_id)
connection.commit()
cursor.execute('SELECT secure_name, uuid_filename FROM Notes WHERE user_id = ?'
    , [user_id])
notes = []
rows = cursor.fetchall()
for row in rows:
notes.append({'file_id': row[1].split('.')[0], 'name': row[0]})
