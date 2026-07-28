def view_header_get(self, cr, user, view_id, view_type, context=None):...
if context is None:
context = {}
res = super(product_product, self).view_header_get(cr, user, view_id,
    view_type, context)
if res:
return res
if context.get('active_id', False) and context.get('active_model'
return _('Products: ') + self.pool.get('stock.location').browse(cr, user,
    context['active_id'], context).name
return res
