def test_float(self):...
value = 1234.567
self.cursor.execute('create table t1(n float)')
self.cursor.execute('insert into t1 values (?)', value)
result = self.cursor.execute('select n from t1').fetchone()[0]
self.assertEqual(result, value)
