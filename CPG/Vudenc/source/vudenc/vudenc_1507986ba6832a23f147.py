def test_p1_not_valid(self):...
"""docstring"""
q = 'TRUNCATE TABLE players;'
tools.query(q)
self.assertEqual(dummy_player(player_name='Double Quarder', country=
    'Playland'), 0)
q = 'SELECT * FROM matches ORDER BY id LIMIT 1'
p = tools.query(q)
i1 = p[0][0]
self.assertEqual(dummy_player(player_name='Big Mac Sauce', country=
    'Playland'), 0)
q = 'SELECT * FROM matches ORDER BY id LIMIT 1'
p = tools.query(q)
i2 = str(p[0][0])
i1 = str(i1 + 2)
tournament.reportMatch(p1=i1, p2=i2)
