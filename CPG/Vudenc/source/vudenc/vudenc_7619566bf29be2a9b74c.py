def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=...
res = super(product_product, self).fields_view_get(cr, uid, view_id,
    view_type, context, toolbar=toolbar, submenu=submenu)
if context is None:
context = {}
if 'location' in context and context['location']:
location_info = self.pool.get('stock.location').browse(cr, uid, context[
    'location'])
return res
fields = res.get('fields', {})
if fields:
if location_info.usage == 'supplier':
if fields.get('virtual_available'):
if location_info.usage == 'internal':
res['fields']['virtual_available']['string'] = _('Future Receptions')
if fields.get('qty_available'):
if fields.get('virtual_available'):
if location_info.usage == 'customer':
res['fields']['qty_available']['string'] = _('Received Qty')
res['fields']['virtual_available']['string'] = _('Future Stock')
if fields.get('virtual_available'):
if location_info.usage == 'inventory':
res['fields']['virtual_available']['string'] = _('Future Deliveries')
if fields.get('qty_available'):
if fields.get('virtual_available'):
if location_info.usage == 'procurement':
res['fields']['qty_available']['string'] = _('Delivered Qty')
res['fields']['virtual_available']['string'] = _('Future P&L')
if fields.get('qty_available'):
if fields.get('virtual_available'):
if location_info.usage == 'production':
res['fields']['qty_available']['string'] = _('P&L Qty')
res['fields']['virtual_available']['string'] = _('Future Qty')
if fields.get('qty_available'):
if fields.get('virtual_available'):
res['fields']['qty_available']['string'] = _('Unplanned Qty')
res['fields']['virtual_available']['string'] = _('Future Productions')
if fields.get('qty_available'):
res['fields']['qty_available']['string'] = _('Produced Qty')
