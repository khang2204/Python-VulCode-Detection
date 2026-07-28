def f():...
self.cursor.execute('create table t1 (word varchar (100))')
words = set(['a'])
self.cursor.execute('insert into t1 (word) VALUES (?)', [words])
