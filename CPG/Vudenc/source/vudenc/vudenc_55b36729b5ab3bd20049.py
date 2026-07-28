import sqlite3, os
script_dir = os.path.dirname(__file__)
rel_path = 'database/main.db'
database = sqlite3.connect(os.path.join(script_dir, rel_path), timeout=1)
database.row_factory = sqlite3.Row
db = database.cursor()
def getPlayer(player):...
db.execute("SELECT * FROM players WHERE Name = '%s' COLLATE NOCASE" % player)
playerstats = dict(db.fetchone())
return playerstats
