def get_accounts(self, cr, uid, item_ids, company_id, context=None):...
"""docstring"""
if context is None:
context = {}
sub_items_ids = self.get_sub_items(cr, item_ids)
sub_items = self.browse(cr, uid, sub_items_ids, context=context)
ids = []
for subitem in sub_items:
ids += [a.id for a in subitem.account]
account_obj = self.pool.get('account.account')
account_flat_list = account_obj.get_children_flat_list(cr, uid, ids,
    company_id, context=context)
return account_flat_list
