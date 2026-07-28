def test_no_players(self):...
"""docstring"""
q = 'TRUNCATE TABLE players;'
tools.query(q)
tournament.swissPairings()
