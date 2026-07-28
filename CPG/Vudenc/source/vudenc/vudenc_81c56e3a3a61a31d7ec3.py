def test_row_slicing(self):...
self.cursor.execute('create table t1(a int, b int, c int, d int)')
self.cursor.execute('insert into t1 values(1,2,3,4)')
row = self.cursor.execute('select * from t1').fetchone()
result = row[:]
self.assertTrue(result is row)
result = row[:-1]
self.assertEqual(result, (1, 2, 3))
result = row[0:4]
self.assertTrue(result is row)
