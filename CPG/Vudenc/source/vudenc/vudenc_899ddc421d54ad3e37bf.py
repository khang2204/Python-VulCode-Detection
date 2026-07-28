def reportMatch(winner, loser):...
"""docstring"""
c = connect()
cur = c.cursor()
def _checkPairing():...
if winner == loser:
q = (
    """
        SELECT COUNT(*) FROM matches
        WHERE (matches.winner_id = %s AND matches.loser_id = %s)
              OR (matches.winner_id = %s AND matches.loser_id = %s);
        """
     % (winner, loser, loser, winner))
cur.execute(q)
if cur.fetchone()[0] > 0:
_checkPairing()
cur.execute('INSERT INTO matches(winner_id, loser_id) VALUES (%s, %s)', (
    winner, loser))
c.commit()
c.close()
