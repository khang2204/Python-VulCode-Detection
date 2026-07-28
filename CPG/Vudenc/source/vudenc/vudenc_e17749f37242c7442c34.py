@api.model...
"""docstring"""
prod_obj = self.env['product.template']
prods = prod_obj.search([('parent_price_product', '!=', False)])
for prod in prods:
default_code = prod.parent_price_product
parent = prod_obj.search([('default_code', '=', default_code)])
if parent and parent.list_price != prod.list_price:
cost = parent.list_price / 10
prod.set_prices(cost, 'EFACEC', price=parent.list_price)
_logger.info('setting price product %s' % prod.default_code)
