@classmethod...
assert engine
s = text(
    'SELECT user_id, username, hashed_password, roll_id FROM users WHERE username = :username AND expire_date is null'
    )
connection = engine.connect()
rc = connection.execute(s, username=username).fetchone()
if rc is not None:
rc = User(rc[0], rc[1], rc[2].decode('utf-8'), rc[3])
connection.close()
return rc
