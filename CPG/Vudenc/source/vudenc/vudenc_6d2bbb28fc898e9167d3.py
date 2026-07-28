def countPlayers():...
"""docstring"""
conn = connect()
table = 'players'
c = conn.cursor()
c.execute('SELECT COUNT(playerID) FROM %s;' % (table,))
result = c.fetchone()[0]
conn.commit()
conn.close()
return result
