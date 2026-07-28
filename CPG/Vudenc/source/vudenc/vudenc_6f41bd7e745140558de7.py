def test_view_select(self):...
self.cursor.execute('create table t1(c1 int identity(1, 1), c2 varchar(50))')
for i in range(3):
self.cursor.execute('insert into t1(c2) values (?)', 'string%s' % i)
self.cursor.execute('create view t2 as select * from t1')
self.cursor.execute('select * from t2')
rows = self.cursor.fetchall()
self.assertTrue(rows is not None)
self.assertTrue(len(rows) == 3)
