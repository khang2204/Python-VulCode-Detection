def get_real_values(self, cr, uid, item, periods, company_id, currency_id,...
"""docstring"""
if context is None:
context = {}
result = 0.0
currency_obj = self.pool.get('res.currency')
move_line_obj = self.pool.get('account.move.line')
accounts = self.get_accounts(cr, uid, [item.id], company_id, context)
move_line_ids = move_line_obj.search(cr, uid, [('period_id', 'in', [p.id for
    p in periods]), ('account_id', 'in', accounts)], context=context)
move_lines = move_line_obj.browse(cr, uid, move_line_ids, context=context)
for line in move_lines:
line_currency_id = line.company_id.currency_id.id
return result
if line.debit != 0:
amount = line.debit
amount = line.credit
sign = -1
sign = 1
ctx = context.copy()
ctx['date'] = change_date.strptime(DEFAULT_SERVER_DATE_FORMAT)
result += sign * currency_obj.compute(cr, uid, line_currency_id,
    currency_id, amount, context=ctx)
