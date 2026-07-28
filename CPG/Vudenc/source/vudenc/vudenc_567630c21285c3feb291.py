def remove_item(self, item):...
"""docstring"""
r = self.cursor.execute('delete from items where itemname = "%s"' % item)
self.connection.commit()
