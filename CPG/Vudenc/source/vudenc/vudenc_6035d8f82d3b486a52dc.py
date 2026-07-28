def countPlayers():...
"""docstring"""
c = connect()
cur = c.cursor()
cur.execute('SELECT COUNT(*) from players;')
res = cur.fetchone()[0]
c.close()
return res
