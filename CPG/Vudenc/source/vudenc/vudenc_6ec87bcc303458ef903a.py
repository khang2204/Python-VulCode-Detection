def add_translation(self, trid):...
"""docstring"""
if self.connection:
self.cursor.execute(
    'insert into itemtranslation (itemid, itemlanguageid, translation) values ("%s", "%s", "%s")'
     % (trid[0], trid[1], trid[2]))
self.connection.commit()
