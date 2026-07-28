def test_fixed_unicode(self):...
value = u'tësting'
self.cursor.execute('create table t1(s nchar(7))')
self.cursor.execute('insert into t1 values(?)', u'tësting')
v = self.cursor.execute('select * from t1').fetchone()[0]
self.assertEqual(type(v), unicode)
self.assertEqual(len(v), len(value))
self.assertEqual(v, value)
