@api.model...
"""docstring"""
if args is None:
args = []
if name:
res = self.search([('ref', 'like', name)], limit=limit)
res = self.search(args, limit=limit)
if not res:
return res.name_get()
res = self.search(['|', ('name', '%', name), ('name', 'ilike', name)],
    order=u"similarity(res_partner.name, '%s') DESC" % name, limit=limit)
if not res:
res = self.search([('email', 'ilike', name)], limit=limit)
