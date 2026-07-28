def test_row_equal(self):...
self.cursor.execute('create table t1(n int, s varchar(20))')
self.cursor.execute("insert into t1 values (1, 'test')")
row1 = self.cursor.execute('select n, s from t1').fetchone()
row2 = self.cursor.execute('select n, s from t1').fetchone()
b = row1 == row2
self.assertEqual(b, True)
