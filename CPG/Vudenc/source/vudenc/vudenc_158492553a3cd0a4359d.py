def vouchPlayer(vouched):...
db.execute('SELECT MAX(ID) as max_id from players')
player = db.fetchone()
ID = player[0]
NewID = ID + 1
db.execute('INSERT INTO players VALUES (?, ?, 0, 1500, 0, 0, 0)', (NewID,
    vouched))
database.commit()
