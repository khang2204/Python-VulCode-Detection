def test_retcursor_delete(self):...
self.cursor.execute('create table t1(i int)')
self.cursor.execute('insert into t1 values (1)')
v = self.cursor.execute('delete from t1')
self.assertEqual(v, self.cursor)
