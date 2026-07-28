def playerStandings():...
"""docstring"""
conn = connect()
c = conn.cursor()
table = 'players'
c.execute(
    """SELECT playerID,                                                           
        playerName,                                                                         
        wins,                                                                               
        matchesPlayed FROM %s ORDER BY wins DESC;"""
     % (table,))
result = c.fetchall()
conn.commit()
conn.close()
return result
