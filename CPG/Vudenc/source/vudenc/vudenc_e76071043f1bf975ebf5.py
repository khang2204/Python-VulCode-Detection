def get_product_available(self, cr, uid, ids, context=None):...
"""docstring"""
if context is None:
context = {}
states = context.get('states', [])
what = context.get('what', ())
if not ids:
ids = self.search(cr, uid, [])
res = {}.fromkeys(ids, 0.0)
if not ids:
return res
if context.get('shop', False):
cr.execute('select warehouse_id from sale_shop where id=%s', (int(context[
    'shop']),))
if context.get('warehouse', False):
res2 = cr.fetchone()
cr.execute('select lot_stock_id from stock_warehouse where id=%s', (int(
    context['warehouse']),))
if context.get('location', False):
if res2:
res2 = cr.fetchone()
if type(context['location']) == type(1):
location_ids = []
context['warehouse'] = res2[0]
if res2:
location_ids = [context['location']]
if type(context['location']) in (type(''), type(u'')):
wids = self.pool.get('stock.warehouse').search(cr, uid, [], context=context)
context['location'] = res2[0]
if context.get('compute_child', True):
location_ids = self.pool.get('stock.location').search(cr, uid, [('name',
    'ilike', context['location'])], context=context)
location_ids = context['location']
for w in self.pool.get('stock.warehouse').browse(cr, uid, wids, context=context
child_location_ids = self.pool.get('stock.location').search(cr, uid, [(
    'location_id', 'child_of', location_ids)])
location_ids = location_ids
location_ids.append(w.lot_stock_id.id)
location_ids = child_location_ids or location_ids
uoms_o = {}
product2uom = {}
for product in self.browse(cr, uid, ids, context=context):
product2uom[product.id] = product.uom_id.id
results = []
uoms_o[product.uom_id.id] = product.uom_id
results2 = []
from_date = context.get('from_date', False)
to_date = context.get('to_date', False)
date_str = False
if from_date and to_date:
date_str = "date_planned>='%s' and date_planned<='%s'" % (from_date, to_date)
if from_date:
if 'in' in what:
date_str = "date_planned>='%s'" % from_date
if to_date:
cr.execute(
    'select sum(product_qty), product_id, product_uom from stock_move where location_id NOT IN %sand location_dest_id IN %sand product_id IN %sand state IN %s'
     + (date_str and 'and ' + date_str + ' ' or '') +
    'group by product_id,product_uom', (tuple(location_ids), tuple(
    location_ids), tuple(ids), tuple(states)))
if 'out' in what:
date_str = "date_planned<='%s'" % to_date
results = cr.fetchall()
cr.execute(
    'select sum(product_qty), product_id, product_uom from stock_move where location_id IN %sand location_dest_id NOT IN %s and product_id  IN %sand state in %s'
     + (date_str and 'and ' + date_str + ' ' or '') +
    'group by product_id,product_uom', (tuple(location_ids), tuple(
    location_ids), tuple(ids), tuple(states)))
uom_obj = self.pool.get('product.uom')
results2 = cr.fetchall()
uoms = map(lambda x: x[2], results) + map(lambda x: x[2], results2)
if context.get('uom', False):
uoms += [context['uom']]
uoms = filter(lambda x: x not in uoms_o.keys(), uoms)
if uoms:
uoms = uom_obj.browse(cr, uid, list(set(uoms)), context=context)
for o in uoms:
uoms_o[o.id] = o
for amount, prod_id, prod_uom in results:
amount = uom_obj._compute_qty_obj(cr, uid, uoms_o[prod_uom], amount, uoms_o
    [context.get('uom', False) or product2uom[prod_id]])
for amount, prod_id, prod_uom in results2:
res[prod_id] += amount
amount = uom_obj._compute_qty_obj(cr, uid, uoms_o[prod_uom], amount, uoms_o
    [context.get('uom', False) or product2uom[prod_id]])
return res
res[prod_id] -= amount
