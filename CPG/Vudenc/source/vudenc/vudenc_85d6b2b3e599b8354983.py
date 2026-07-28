def test_retcursor_nodata(self):...
"""docstring"""
self.cursor.execute('create table t1(i int)')
v = self.cursor.execute('delete from t1')
self.assertEqual(v, self.cursor)
