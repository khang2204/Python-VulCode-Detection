def test_description(self):...
"""docstring"""
self.cursor.execute('create table t1(n int, s text)')
self.cursor.execute("insert into t1 values (1, 'abc')")
self.cursor.execute('select * from t1')
t = self.cursor.description[0]
self.assertEqual(t[0], 'n')
self.assertEqual(t[1], int)
self.assertEqual(t[5], 0)
self.assertEqual(t[6], True)
t = self.cursor.description[1]
self.assertEqual(t[0], 's')
self.assertEqual(t[1], str)
self.assertEqual(t[5], 0)
self.assertEqual(t[6], True)
