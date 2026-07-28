import copy
from operator import itemgetter
from openerp.osv import fields, orm, osv
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from tools.safe_eval import safe_eval
from openerp.tools.translate import _
""" Budget Item

    This is a link between budgets and financial accounts. """
_name = 'budget.item'
_description = 'Budget items'
_order = 'sequence ASC, name ASC'
_columns = {'code': fields.char('Code', required=True), 'name': fields.char
    ('Name', required=True), 'active': fields.boolean('Active'),
    'parent_id': fields.many2one('budget.item', string='Parent Item',
    ondelete='cascade'), 'children_ids': fields.one2many('budget.item',
    'parent_id', string='Children Items'), 'account': fields.many2many(
    'account.account', string='Financial Account'), 'note': fields.text(
    'Notes'), 'calculation': fields.text('Calculation'), 'type': fields.
    selection([('view', 'View'), ('normal', 'Normal')], string='Type',
    required=True), 'sequence': fields.integer('Sequence'), 'style': fields
    .selection([('normal', 'Normal'), ('bold', 'Bold'), ('invisible',
    'Invisible')], string='Style', required=True)}
_defaults = {'active': True, 'type': 'normal', 'style': 'normal'}
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
