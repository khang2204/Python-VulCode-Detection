def add_user(username, password):...
salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in
    range(SALT_LENGTH))
password_hash = multiple_hash_password(password, salt)
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute(
    """INSERT INTO UserData(username, password_hash, salt) 
                      VALUES (?, ?, ?)"""
    , (username, password_hash, salt))
connection.commit()
connection.close()
