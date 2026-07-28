def get_list_items(self, a_list):...
"""docstring"""
return self.cursor.execute(
    'select items.itemid, listitems.amount, items.itemname from items, listitems, lists where lists.listhash = "%s" and listitems.listid = lists.listid and listitems.itemid = items.itemid'
     % a_list)
