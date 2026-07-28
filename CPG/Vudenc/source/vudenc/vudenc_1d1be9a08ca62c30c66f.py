def registerPlayer(name):...
"""docstring"""
conn = connect()
c = conn.cursor()
c.execute("INSERT INTO players (playerName) VALUES ('{}')".format(re.sub(
    "\\'", '', name)))
conn.commit()
conn.close()
