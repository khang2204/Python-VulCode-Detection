def test_int(self):...
value = 1234
self.cursor.execute('create table t1(n int)')
self.cursor.execute('insert into t1 values (?)', value)
result = self.cursor.execute('select n from t1').fetchone()[0]
self.assertEqual(result, value)
