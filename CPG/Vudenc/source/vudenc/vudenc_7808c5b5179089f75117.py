def CreateGame(Pod):...
db.execute('INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
    Pod)
database.commit()
