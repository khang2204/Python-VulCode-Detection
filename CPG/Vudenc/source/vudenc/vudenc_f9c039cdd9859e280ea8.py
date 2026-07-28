def getGameNewID():...
db.execute('SELECT MAX(ID) AS max_id FROM games')
game = db.fetchone()
NewID = int(game[0]) + 1
return NewID
