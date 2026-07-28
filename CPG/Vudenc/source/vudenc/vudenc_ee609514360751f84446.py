def test_negative_bigint(self):...
input = -430000000
self.cursor.execute('create table t1(d bigint)')
self.cursor.execute('insert into t1 values (?)', input)
result = self.cursor.execute('select d from t1').fetchone()[0]
self.assertEqual(result, input)
