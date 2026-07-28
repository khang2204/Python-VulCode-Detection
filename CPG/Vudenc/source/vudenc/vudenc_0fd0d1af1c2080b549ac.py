def getRunning():...
db.execute("SELECT * FROM games WHERE Running = 'Yes'")
running = db.fetchall()
return running
