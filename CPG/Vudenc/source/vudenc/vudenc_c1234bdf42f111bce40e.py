def f():...
self.cursor.execute('create table t1 (word varchar (100))')
words = set(['a'])
self.cursor.executemany('insert into t1 (word) values (?)', [words])
