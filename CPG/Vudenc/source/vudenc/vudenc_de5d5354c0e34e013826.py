@classmethod...
assert engine
s = text(
    'SELECT * FROM users WHERE username = :username AND expire_date is null')
connection = engine.connect()
rc = False if connection.execute(s, username=username).fetchone(
    ) is None else True
connection.close()
return rc
