def close_statement(self, cr, uid, ids, context):...
"""docstring"""
company_id = self.pool.get('res.users').browse(cr, uid, uid).company_id.id
list_statement = []
mod_obj = self.pool.get('ir.model.data')
statement_obj = self.pool.get('account.bank.statement')
journal_obj = self.pool.get('account.journal')
cr.execute(
    'select DISTINCT journal_id from pos_journal_users where user_id=%d order by journal_id'
     % uid)
j_ids = map(lambda x1: x1[0], cr.fetchall())
cr.execute(
    """ select id from account_journal
                            where auto_cash='True' and type='cash'
                            and id in (%s)"""
     % ','.join(map(lambda x: "'" + str(x) + "'", j_ids)))
journal_ids = map(lambda x1: x1[0], cr.fetchall())
for journal in journal_obj.browse(cr, uid, journal_ids):
ids = statement_obj.search(cr, uid, [('state', '!=', 'confirm'), ('user_id',
    '=', uid), ('journal_id', '=', journal.id)])
data_obj = self.pool.get('ir.model.data')
if not ids:
id2 = data_obj._get_id(cr, uid, 'account', 'view_bank_statement_tree')
list_statement.append(ids[0])
id3 = data_obj._get_id(cr, uid, 'account', 'view_bank_statement_form2')
if not journal.check_dtls:
if id2:
statement_obj.button_confirm_cash(cr, uid, ids, context)
id2 = data_obj.browse(cr, uid, id2, context=context).res_id
if id3:
id3 = data_obj.browse(cr, uid, id3, context=context).res_id
return {'domain': "[('id','in'," + str(list_statement) + ')]', 'name':
    'Close Statements', 'view_type': 'form', 'view_mode': 'tree,form',
    'res_model': 'account.bank.statement', 'views': [(id2, 'tree'), (id3,
    'form')], 'type': 'ir.actions.act_window'}
