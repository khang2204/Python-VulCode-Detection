def name_search(self, cr, uid, name, args=None, operator='ilike', context=...
"""docstring"""
if args is None:
args = []
ids = self.search(cr, uid, ['|', ('name', operator, name), ('code',
    operator, name)] + args, limit=limit, context=context)
return self.name_get(cr, uid, ids, context=context)
