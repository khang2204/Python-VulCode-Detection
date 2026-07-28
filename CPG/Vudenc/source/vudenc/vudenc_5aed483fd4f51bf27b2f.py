@api.multi...
"""docstring"""
for prod in self:
invoice_line = self.closest_invoice_line(prod, datetime.today().strftime(
    '%Y-%m-%d'))
invoice_price = 0
if invoice_line and invoice_line.price_unit:
invoice_price = invoice_line.price_unit
prod.system_cost = invoice_price
invoice_price *= 1 - invoice_line.discount / 100
_logger.info('Setting invoice cost $ %d - %s' % (invoice_price, prod.
    default_code))
invoice_price *= 1 + invoice_line.invoice_discount
if invoice_line.invoice_id.partner_id.ref == 'BULONFER':
invoice_price *= 1 - 0.05
