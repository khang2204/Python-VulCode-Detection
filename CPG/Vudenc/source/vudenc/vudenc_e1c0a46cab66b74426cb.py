def deleteMatches():...
"""docstring"""
conn = connect()
c = conn.cursor()
table = 'matches'
playerTable = 'players'
c.execute('DELETE FROM %s;' % (table,))
c.execute(
    """UPDATE %s SET wins = 0, 
        loss = 0, matchesPlayed = 0""" % (
    playerTable,))
conn.commit()
conn.close()
