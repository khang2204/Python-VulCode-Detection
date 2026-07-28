import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api
_logger = logging.getLogger(__name__)
_name = 'event.event'
_inherit = ['event.event']
fit_is_participating = fields.Boolean('Is Participating', compute=
    '_fit_compute_is_participating')
website_published = fields.Boolean(default=True)
fit_day_of_week = fields.Char(string='Dag', default='')
fit_repetition_enabled = fields.Boolean(string='Herhalen?', default=False)
fit_repetition = fields.Selection([('daily', 'Dagelijks'), ('weekly',
    'Wekelijks'), ('monthly', 'Maandelijks')], string='Schema herhaling')
def _fit_compute_is_participating(self):...
if self.env.user != self.env.ref('base.public_user'):
email = self.env.user.partner_id.email
@api.onchange('date_begin')...
for event in self:
start_date = self.date_begin_located
domain = ['&', '|', ('email', '=', email), ('partner_id', '=', self.env.
    user.partner_id.id), ('event_id', '=', event.id), ('state', '=', 'open')]
if start_date:
count = self.env['event.registration'].search_count(domain)
self.fit_day_of_week = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S'
    ).strftime('%a')
def get_attendee_list(self):...
if count > 0:
attendee_list = str('')
event.fit_is_participating = True
event.fit_is_participating = False
counter = 1
reg_ids = self.sudo().registration_ids
reg_ids = sorted(reg_ids, key=lambda x: x.date_open, reverse=False)
for registration in reg_ids:
if registration.state == 'open':
return attendee_list
if counter == 1:
attendee_list += registration.partner_id.sudo().name
attendee_list += ', ' + registration.partner_id.sudo().name
counter += 1
