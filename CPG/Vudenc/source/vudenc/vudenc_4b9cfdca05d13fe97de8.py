def reportMatch(winner, loser):...
"""docstring"""
conn = connect()
c = conn.cursor()
c.execute(
    """INSERT INTO matches (winner, loser)                                        
        VALUES ('%i', '%i')"""
     % (winner, loser))
c.execute(
    """UPDATE players SET wins = wins + 1,                                        
        matchesPlayed = matchesPlayed + 1                                                   
        WHERE playerID = %s"""
     % (winner,))
c.execute(
    """UPDATE players SET loss = loss + 1,                                        
        matchesPlayed = matchesPlayed + 1                                                   
        WHERE playerID = %s"""
     % (loser,))
conn.commit()
conn.close()
