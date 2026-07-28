def test_subquery_params(self):...
"""docstring"""
self.cursor.execute('create table t1(id integer, s varchar(20))')
self.cursor.execute('insert into t1 values (?,?)', 1, 'test')
row = self.cursor.execute(
    """
                                  select x.id
                                  from (
                                    select id
                                    from t1
                                    where s = ?
                                      and id between ? and ?
                                   ) x
                                   """
    , 'test', 1, 10).fetchone()
self.assertNotEqual(row, None)
self.assertEqual(row[0], 1)
