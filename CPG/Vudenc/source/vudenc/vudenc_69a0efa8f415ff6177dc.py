def find_all_items(self, langid):...
"""docstring"""
if langid[0] == '0':
return self.cursor.execute('select * from item')
return self.cursor.execute(
    'select item.id, item.shoppinglistid, item.name,                 itemtranslation.id, itemtranslation.itemid, itemtranslation.itemlanguageid,                 itemtranslation.translation                 from item                 left join itemtranslation                 on itemtranslation.itemlanguageid = "%s" and itemtranslation.itemid = item.id'
     % langid[0])
