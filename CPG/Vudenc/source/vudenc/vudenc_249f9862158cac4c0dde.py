def test_p2_not_valid(self):...
"""docstring"""
q = 'TRUNCATE TABLE players;'
tools.query(q)
self.assertEqual(dummy_player(player_name='Fissh Fillay', country=
    'Playland'), 0)
q = 'SELECT * FROM matches ORDER BY id LIMIT 1'
p = tools.query(q)
i1 = str(p[0][0])
self.assertEqual(dummy_player(player_name='Kulv Sangwich', country=
    'Playland'), 0)
q = 'SELECT * FROM matches ORDER BY id LIMIT 1'
p = tools.query(q)
i2 = p[0][0]
i2 = str(i2 + 2)
tournament.reportMatch(p1=i1, p2=i2)
