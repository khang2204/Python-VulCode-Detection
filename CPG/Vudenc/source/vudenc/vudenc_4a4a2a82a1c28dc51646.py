def createDatabase():...
c, conn = getConnection()
c.execute(
    """CREATE TABLE if not exists npc
				 (date text, user text, race text, class text, sex text, level INTEGER, image text, legit INTEGER)"""
    )
c.execute(
    """CREATE TABLE if not exists usage
				 (id INTEGER PRIMARY KEY AUTOINCREMENT, date text, user text, command text)"""
    )
conn.commit()
conn.close()
