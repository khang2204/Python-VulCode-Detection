def _fit_compute_is_participating(self):...
if self.env.user != self.env.ref('base.public_user'):
email = self.env.user.partner_id.email
for event in self:
domain = ['&', '|', ('email', '=', email), ('partner_id', '=', self.env.
    user.partner_id.id), ('event_id', '=', event.id), ('state', '=', 'open')]
count = self.env['event.registration'].search_count(domain)
if count > 0:
event.fit_is_participating = True
event.fit_is_participating = False
