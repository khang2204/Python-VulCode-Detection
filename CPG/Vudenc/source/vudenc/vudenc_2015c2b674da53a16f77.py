def test_rowcount_delete(self):...
self.assertEqual(self.cursor.rowcount, -1)
self.cursor.execute('create table t1(i int)')
count = 4
for i in range(count):
self.cursor.execute('insert into t1 values (?)', i)
self.cursor.execute('delete from t1')
self.assertEqual(self.cursor.rowcount, count)
