def list_items_not_in_store(self, storeind):...
"""docstring"""
r = self.cursor.execute(
    'select items.itemid, items.itemname from items where items.itemid not in (select shoppingorder.itemid from shoppingorder, store where store.storeid = "%s" and store.storeid = shoppingorder.storeid) order by items.itemname'
     % storeind).fetchall()
return r
