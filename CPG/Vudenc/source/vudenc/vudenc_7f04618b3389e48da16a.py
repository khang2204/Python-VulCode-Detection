def addtolist(self, listhash, itemind, amount):...
"""docstring"""
listid = self.cursor.execute(
    'select listid, listhash from lists where listhash = "%s"' % listhash
    ).fetchall()[0]
t = listid[0], itemind, amount
self.cursor.execute(
    'insert into listitems (listid, itemid, amount) values (?, ?, ?)', t)
self.connection.commit()
r = self.cursor.execute(
    'select listitemsid, listid, itemid, amount from listitems where listid="%s" and itemid = "%s"'
     % (listid[0], itemind)).fetchall()[0]
return r
