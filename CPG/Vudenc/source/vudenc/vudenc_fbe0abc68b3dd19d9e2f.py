def do_change_standard_price(self, cr, uid, ids, datas, context={}):...
"""docstring"""
location_obj = self.pool.get('stock.location')
move_obj = self.pool.get('account.move')
move_line_obj = self.pool.get('account.move.line')
new_price = datas.get('new_price', 0.0)
stock_output_acc = datas.get('stock_output_account', False)
stock_input_acc = datas.get('stock_input_account', False)
journal_id = datas.get('stock_journal', False)
product_obj = self.browse(cr, uid, ids)[0]
account_variation = product_obj.categ_id.property_stock_variation
account_variation_id = account_variation and account_variation.id or False
if not account_variation_id:
move_ids = []
loc_ids = location_obj.search(cr, uid, [('usage', '=', 'internal')])
for rec_id in ids:
for location in location_obj.browse(cr, uid, loc_ids):
return move_ids
c = context.copy()
self.write(cr, uid, rec_id, {'standard_price': new_price})
c.update({'location': location.id, 'compute_child': False})
product = self.browse(cr, uid, rec_id, context=c)
qty = product.qty_available
diff = product.standard_price - new_price
if not diff:
if qty:
company_id = location.company_id and location.company_id.id or False
if not company_id:
if not journal_id:
journal_id = (product.categ_id.property_stock_journal and product.categ_id.
    property_stock_journal.id or False)
if not journal_id:
move_id = move_obj.create(cr, uid, {'journal_id': journal_id, 'company_id':
    company_id})
move_ids.append(move_id)
if diff > 0:
if not stock_input_acc:
if diff < 0:
stock_input_acc = product.product_tmpl_id.property_stock_account_input.id
if not stock_input_acc:
if not stock_output_acc:
stock_input_acc = product.categ_id.property_stock_account_input_categ.id
if not stock_input_acc:
stock_output_acc = product.product_tmpl_id.property_stock_account_output.id
if not stock_output_acc:
amount_diff = qty * diff
stock_output_acc = product.categ_id.property_stock_account_output_categ.id
if not stock_output_acc:
move_line_obj.create(cr, uid, {'name': product.name, 'account_id':
    stock_input_acc, 'debit': amount_diff, 'move_id': move_id})
amount_diff = qty * -diff
move_line_obj.create(cr, uid, {'name': product.categ_id.name, 'account_id':
    account_variation_id, 'credit': amount_diff, 'move_id': move_id})
move_line_obj.create(cr, uid, {'name': product.name, 'account_id':
    stock_output_acc, 'credit': amount_diff, 'move_id': move_id})
move_line_obj.create(cr, uid, {'name': product.categ_id.name, 'account_id':
    account_variation_id, 'debit': amount_diff, 'move_id': move_id})
