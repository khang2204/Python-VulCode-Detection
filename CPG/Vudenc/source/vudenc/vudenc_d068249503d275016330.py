def open_statement(self, cr, uid, ids, context):...
"""docstring"""
list_statement = []
mod_obj = self.pool.get('ir.model.data')
company_id = self.pool.get('res.users').browse(cr, uid, uid).company_id.id
statement_obj = self.pool.get('account.bank.statement')
sequence_obj = self.pool.get('ir.sequence')
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
if len(ids):
id2 = data_obj._get_id(cr, uid, 'account', 'view_bank_statement_tree')
number = ''
id3 = data_obj._get_id(cr, uid, 'account', 'view_bank_statement_form2')
if journal.sequence_id:
if id2:
number = sequence_obj.get_id(cr, uid, journal.sequence_id.id)
number = sequence_obj.get(cr, uid, 'account.bank.statement')
id2 = data_obj.browse(cr, uid, id2, context=context).res_id
if id3:
statement_id = statement_obj.create(cr, uid, {'journal_id': journal.id,
    'company_id': company_id, 'user_id': uid, 'state': 'open', 'name':
    number, 'starting_details_ids': statement_obj._get_cash_close_box_lines
    (cr, uid, [])})
id3 = data_obj.browse(cr, uid, id3, context=context).res_id
return {'domain': "[('state','=','open')]", 'name': 'Open Statement',
    'view_type': 'form', 'view_mode': 'tree,form', 'res_model':
    'account.bank.statement', 'views': [(id2, 'tree'), (id3, 'form')],
    'type': 'ir.actions.act_window'}
statement_obj.button_open(cr, uid, [statement_id], context)
