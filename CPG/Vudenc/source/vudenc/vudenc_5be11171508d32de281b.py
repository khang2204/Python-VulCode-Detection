def find_item_id(self, idid):...
"""docstring"""
return self.cursor.execute(
    'select item.id, item.shoppinglistid, item.name,             itemtranslation.id, itemtranslation.itemid, itemtranslation.itemlanguageid,             itemtranslation.translation             from item, itemtranslation             where item.id = "%s" and itemtranslation.itemlanguageid = "%s" and itemtranslation.itemid = item.id'
     % (idid[0], idid[1]))
