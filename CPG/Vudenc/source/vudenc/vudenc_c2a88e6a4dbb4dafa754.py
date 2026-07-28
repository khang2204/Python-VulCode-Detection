@api.model...
"""docstring"""
fuzzy_search = False
for arg in args:
if arg[0] == 'name' and arg[1] == '%':
if fuzzy_search:
fuzzy_search = arg[2]
order = u"similarity(res_partner.name, '%s') DESC" % fuzzy_search
return super(ResPartner, self).search(args, offset, limit, order, count)
