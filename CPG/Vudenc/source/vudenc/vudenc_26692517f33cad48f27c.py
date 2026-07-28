def update_item(self, itemid, itemname):...
"""docstring"""
self.cursor.execute('update items set itemname = "%s" where itemid = "%s"' %
    (itemname, itemid))
self.connection.commit()
