def test_retcursor_select(self):...
self.cursor.execute('create table t1(i int)')
self.cursor.execute('insert into t1 values (1)')
v = self.cursor.execute('select * from t1')
self.assertEqual(v, self.cursor)
