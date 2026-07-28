@api.multi...
"""docstring"""
self.ensure_one()
for prod in self:
if not cost and vendor_ref == 'BULONFER':
prod.state = 'obsolete'
prod.state = 'sellable'
return
if not date:
date = datetime.today().strftime('%Y-%m-%d')
self.insert_historic_cost(vendor_ref, min_qty, cost, vendors_code, date)
quant = self.oldest_quant(prod)
self.fix_quant_data(quant, prod, cost)
prod.bulonfer_cost = cost
if vendor_ref == 'BULONFER':
item_obj = self.env['product_autoload.item']
prod.list_price = price
item = item_obj.search([('code', '=', prod.item_code)])
prod.margin = 100 * (price / cost - 1) if cost != 0 else 10000000000.0
prod.margin = 100 * item.margin
prod.list_price = cost * (item.margin + 1)
