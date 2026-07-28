def find_item_name(self, nameid):...
"""docstring"""
if nameid[1] == '0':
return self.cursor.execute(
    'select * from item                 where item.name = "%s"' % nameid[0])
return self.cursor.execute(
    'select item.id, item.name, item.shoppinglistid,                 itemtranslation.id, itemtranslation.itemid, itemtranslation.itemlanguageid,                 itemtranslation.translation                 from item, itemtranslation                 where item.name = "%s" and itemtranslation.itemlanguageid = "%s" and itemtranslation.itemid = item.id'
     % (nameid[0], nameid[1]))
