from openerp import api, fields, models
_inherit = 'crm.lead'
phonecall_ids = fields.One2many(comodel_name='crm.phonecall', inverse_name=
    'opportunity_id', string='Phonecalls')
phonecall_count = fields.Integer(compute='_phonecall_count', string=
    'Phonecalls')
@api.multi...
for lead in self:
lead.phonecall_count = self.env['crm.phonecall'].search_count([(
    'opportunity_id', '=', lead.id)])
