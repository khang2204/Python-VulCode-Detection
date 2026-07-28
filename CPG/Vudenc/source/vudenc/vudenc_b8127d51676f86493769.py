def _product_available(self, cr, uid, ids, field_names=None, arg=False,...
"""docstring"""
if not field_names:
field_names = []
if context is None:
context = {}
res = {}
for id in ids:
res[id] = {}.fromkeys(field_names, 0.0)
for f in field_names:
c = context.copy()
return res
if f == 'qty_available':
c.update({'states': ('done',), 'what': ('in', 'out')})
if f == 'virtual_available':
c.update({'states': ('confirmed', 'waiting', 'assigned', 'done'), 'what': (
    'in', 'out')})
if f == 'incoming_qty':
c.update({'states': ('confirmed', 'waiting', 'assigned'), 'what': ('in',)})
if f == 'outgoing_qty':
c.update({'states': ('confirmed', 'waiting', 'assigned'), 'what': ('out',)})
stock = self.get_product_available(cr, uid, ids, context=c)
for id in ids:
res[id][f] = stock.get(id, 0.0)
