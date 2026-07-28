def list_items_in_order(self, storeind):...
"""docstring"""
r = self.cursor.execute(
    'select shoppingorder.sorder, shoppingorder.storeid, shoppingorder.itemid, store.storeid, store.storename, items.itemid, items.itemname from shoppingorder, store, items where (store.storeid = %s and items.itemid = shoppingorder.itemid and shoppingorder.storeid = store.storeid) order by shoppingorder.sorder'
     % storeind).fetchall()
return r
