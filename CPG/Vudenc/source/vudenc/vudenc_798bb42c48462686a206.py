def test_option_delete(self):...
"""docstring"""
q = 'SELECT * FROM matches ORDER BY id LIMIT 1'
r = tools.query(q)
s = str(r[0][0])
self.assertEquals(tournament.deletePlayer(player=s), 0)
