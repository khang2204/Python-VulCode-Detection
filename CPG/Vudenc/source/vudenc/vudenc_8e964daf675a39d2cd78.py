def test_large_update_nodata(self):...
self.cursor.execute('create table t1(a blob)')
hundredkb = 'x' * 100 * 1024
self.cursor.execute('update t1 set a=? where 1=0', (hundredkb,))
