def get_real_values_from_analytic_accounts(self, cr, uid, item_id, periods,...
"""docstring"""
if context is None:
context = {}
budget_line_obj = self.pool.get('budget.line')
budget_lines = budget_line_obj.filter_by_items(cr, uid, lines, [item_id],
    context=context)
aa_ids = budget_line_obj.get_analytic_accounts(cr, uid, budget_lines,
    company_id, context=context)
general_accounts_ids = self.get_accounts(cr, uid, [item_id], company_id,
    context=context)
start_date = None
end_date = None
for period in periods:
if start_date is None or start_date > period.date_start:
aa_lines_obj = self.pool.get('account.analytic.line')
start_date = period.date_start
if end_date is None or end_date < period.date_stop:
aa_lines_ids = aa_lines_obj.search(cr, uid, [('date', '>=', start_date), (
    'date', '<=', end_date), ('general_account_id', 'in',
    general_accounts_ids), ('account_id', 'in', aa_ids)], context=context)
end_date = period.date_stop
aa_lines = aa_lines_obj.browse(cr, uid, aa_lines_ids, context=context)
result = 0
currency_obj = self.pool.get('res.currency')
ctx = context.copy()
ctx['date'] = change_date.strptime(DEFAULT_SERVER_DATE_FORMAT)
for line in aa_lines:
from_ccy_id = line.general_account_id.company_id.currency_id.id
return result
result += currency_obj.compute(cr, uid, from_ccy_id, currency_id, line.
    amount, context=ctx)
