def add_shoppinglist(self, slist):...
"""docstring"""
t = slist,
self.cursor.execute('insert into lists (listhash) values (?)', t)
self.connection.commit()
r = self.cursor.execute(
    'select listid, listhash from lists where listhash = "%s"' % slist
    ).fetchall()[0]
return r
