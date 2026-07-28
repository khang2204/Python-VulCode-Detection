import logging
from odoo import fields, api, exceptions, _
from odoo import SUPERUSER_ID
from odoo.tools.safe_eval import safe_eval
from odoo.addons.base_crapo_workflow.mixins.crapo_readonly_view_mixin import ReadonlyViewMixin
"""
        Mixin class that can be used to define an Odoo Model eligible
        to be managed by a Crapo Automaton

        Should be use as a mixin class in existing objects
    """
_readonly_domain = (
    "[('crapo_readonly_fields', 'like', ',{},'.format(field_name))]")
_readonly_fields_to_add = ['crapo_readonly_fields']
automaton = fields.Many2one(comodel_name='crapo.automaton', string=
    'Related automaton', help=
    'The automaton describes the various transitions an object can go through between states.'
    , default=lambda self: self._get_model_automaton(), store=True, index=
    True, required=True)
state = fields.Many2one(comodel_name='crapo.state', help=
    'State in which this object is', track_visibility='onchange', domain=lambda
    self: self._get_state_domain(), group_expand='_read_group_states',
    default=lambda self: self._get_default_state(), store=True, index=True,
    required=True)
crapo_readonly_fields = fields.Char(compute=
    '_compute_crapo_readonly_fields', default=',0,')
@api.depends('state')...
for rec in self:
if rec.state.readonly_fields:
@api.model...
rec.crapo_readonly_fields = ',{},'.format(rec.state.readonly_fields)
rec.crapo_readonly_fields = ',0,'
automaton_model = self.env['crapo.automaton']
my_model = self.env['ir.model'].search([('model', '=', self._name)], limit=1)
my_automaton = automaton_model.search([('model_id', '=', my_model.id)], limit=1
    )
if my_automaton:
return my_automaton
return automaton_model.create({'name': 'Automaton for {}'.format(self._name
    ), 'model_id': my_model.id})
