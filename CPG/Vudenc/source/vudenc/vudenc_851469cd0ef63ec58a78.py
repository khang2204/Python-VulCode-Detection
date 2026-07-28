def update_shoppinglist(self, slistid, slisthash):...
self.cursor.execute('update lists set listhash = "%s" where listid = "%s"' %
    (slisthash, slistid))
self.connection.commit()
