def test_option_edit(self):...
"""docstring"""
q = 'SELECT * FROM matches ORDER BY id LIMIT 1'
r = tools.query(q)
s = str(r[0][0])
self.assertEquals(tournament.editPlayer(player=s, new_name='Johan Bach',
    new_country='Guam'), 0)
