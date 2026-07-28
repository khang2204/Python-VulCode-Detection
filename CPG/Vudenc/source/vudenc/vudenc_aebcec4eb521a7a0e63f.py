def test_rowcount_nodata(self):...
"""docstring"""
self.cursor.execute('create table t1(i int)')
self.cursor.execute('delete from t1')
self.assertEqual(self.cursor.rowcount, 0)
