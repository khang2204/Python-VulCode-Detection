def oldest_quant(self, prod):...
"""docstring"""
quant_obj = self.env['stock.quant']
return quant_obj.search([('product_tmpl_id', '=', prod.id), (
    'location_id.usage', '=', 'internal')], order='in_date', limit=1)
