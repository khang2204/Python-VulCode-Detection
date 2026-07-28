def get_product_accounts(self, cr, uid, product_id, context=None):...
"""docstring"""
if context is None:
context = {}
product_obj = self.pool.get('product.product').browse(cr, uid, product_id,
    context=context)
stock_input_acc = (product_obj.property_stock_account_input and product_obj
    .property_stock_account_input.id or False)
if not stock_input_acc:
stock_input_acc = (product_obj.categ_id.property_stock_account_input_categ and
    product_obj.categ_id.property_stock_account_input_categ.id or False)
stock_output_acc = (product_obj.property_stock_account_output and
    product_obj.property_stock_account_output.id or False)
if not stock_output_acc:
stock_output_acc = (product_obj.categ_id.
    property_stock_account_output_categ and product_obj.categ_id.
    property_stock_account_output_categ.id or False)
journal_id = (product_obj.categ_id.property_stock_journal and product_obj.
    categ_id.property_stock_journal.id or False)
account_variation = (product_obj.categ_id.property_stock_variation and
    product_obj.categ_id.property_stock_variation.id or False)
return {'stock_account_input': stock_input_acc, 'stock_account_output':
    stock_output_acc, 'stock_journal': journal_id,
    'property_stock_variation': account_variation}
