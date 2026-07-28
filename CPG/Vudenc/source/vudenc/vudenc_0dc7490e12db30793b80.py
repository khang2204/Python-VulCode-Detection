def test_negative_row_index(self):...
self.cursor.execute('create table t1(s varchar(20))')
self.cursor.execute('insert into t1 values(?)', '1')
row = self.cursor.execute('select * from t1').fetchone()
self.assertEqual(row[0], '1')
self.assertEqual(row[-1], '1')
