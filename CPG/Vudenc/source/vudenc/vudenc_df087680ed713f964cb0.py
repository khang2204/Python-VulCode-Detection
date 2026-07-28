def update_store(self, storeid, storename):...
self.cursor.execute(
    'update store set storename = "%s" where storeid = "%s"' % (storename,
    storeid))
self.connection.commit()
