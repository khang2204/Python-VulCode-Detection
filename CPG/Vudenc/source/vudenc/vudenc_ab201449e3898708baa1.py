def save(self):...
connection = engine.connect()
trans = connection.begin()
s = text(
    'INSERT INTO users(username, hashed_password, roll_id) VALUES(:username, :hashed_password, :roll_id)'
    )
trans.rollback()
connection.close()
connection.execute(s, username=self.username, hashed_password=self.
    hashed_password, roll_id=self.roll_id)
trans.commit()
