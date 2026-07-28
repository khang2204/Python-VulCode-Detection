def test_display_zero_matches(self):...
"""docstring"""
q = 'TRUNCATE TABLE players;'
tools.query(q)
self.assertEqual(tournament.list_players(), 1)
