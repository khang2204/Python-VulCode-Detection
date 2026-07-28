@api.multi...
"""docstring"""
self.ensure_one()
if isinstance(product, int):
product = self.env['product.product'].browse(product)
ref = self.ref
bvr_reference = '0' * (9 + (7 - len(ref))) + ref
bvr_reference += '0' * 5
bvr_reference += '6'
bvr_reference += '0' * (4 - len(str(product.fund_id))) + str(product.fund_id)
if len(bvr_reference) == 26:
return mod10r(bvr_reference)
