def removefromlist(self, listhash, itemind):...
"""docstring"""
listid = self.cursor.execute(
    'select listid from lists where listhash = "%s"' % listhash).fetchall()[0]
print('removing itemind, listid: %s, %s' % (itemind, listid[0]))
r = self.cursor.execute(
    'delete from listitems where (itemid = "%s" and listid = "%s")' % (
    itemind, listid[0]))
self.connection.commit()
