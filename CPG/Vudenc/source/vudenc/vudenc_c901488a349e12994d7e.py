def test_skip(self):...
self.cursor.execute('create table t1(id int)')
for i in range(1, 5):
self.cursor.execute('insert into t1 values(?)', i)
self.cursor.execute('select id from t1 order by id')
self.assertEqual(self.cursor.fetchone()[0], 1)
self.cursor.skip(2)
self.assertEqual(self.cursor.fetchone()[0], 4)
