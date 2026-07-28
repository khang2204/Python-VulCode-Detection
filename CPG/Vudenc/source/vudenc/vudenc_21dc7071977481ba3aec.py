@api.multi...
"""docstring"""
self.ensure_one()
mv_line_obj = self.env['account.move.line']
move_line_ids = mv_line_obj.search([('partner_id', '=', self.id), (
    'account_id.code', '=', '1050'), ('credit', '>', '0'), (
    'full_reconcile_id', '=', False)])
res = 0
for move_line in move_line_ids:
res += move_line.credit
return res
