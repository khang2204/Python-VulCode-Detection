def _check_recursion(self, cr, uid, ids, context=None, parent=None):...
"""docstring"""
return super(budget_item, self)._check_recursion(cr, uid, ids, parent=
    parent or 'parent_id', context=context)
