def getConnection():...
conn = sqlite3.connect(DATABASE_NAME)
c = conn.cursor()
return c, conn
