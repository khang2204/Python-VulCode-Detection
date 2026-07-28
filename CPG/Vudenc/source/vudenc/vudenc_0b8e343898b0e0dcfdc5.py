def search(self, cr, uid, args, offset=0, limit=None, order=None, context=...
"""docstring"""
if context is None:
context = {}
result = []
parent_result = super(budget_item, self).search(cr, uid, args, offset,
    limit, order, context, count)
if context.get('budget_id'):
budget_obj = self.pool.get('budget.budget')
result = parent_result
budget = budget_obj.browse(cr, uid, context['budget_id'], context=context)
return result
allowed_items = self.get_sub_items(cr, [budget.budget_item_id.id])
result.extend([item for item in parent_result if item in allowed_items])
