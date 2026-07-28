def test_different_bindings(self):...
self.cursor.execute('create table t1(n int)')
self.cursor.execute('create table t2(d datetime)')
self.cursor.execute('insert into t1 values (?)', 1)
self.cursor.execute('insert into t2 values (?)', datetime.now())
