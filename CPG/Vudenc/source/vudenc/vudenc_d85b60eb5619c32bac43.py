@api.onchange('lastname', 'firstname', 'zip', 'email')...
if (self.lastname and self.firstname and self.zip or self.email
partner_duplicates = self.search([('id', '!=', self._origin.id), '|', '&',
    ('email', '=', self.email), ('email', '!=', False), '&', '&', (
    'firstname', 'ilike', self.firstname), ('lastname', 'ilike', self.
    lastname), ('zip', '=', self.zip)])
if partner_duplicates:
self.partner_duplicate_ids = partner_duplicates
new_env = api.Environment(new_cr, self.env.uid, {})
self._origin.with_env(new_env).write({'partner_duplicate_ids': [(6, 0,
    partner_duplicates.ids)]})
return {'warning': {'title': _('Possible existing partners found'),
    'message': _(
    'The partner you want to add may already exist. Please use the "Check duplicates" button to review it.'
    )}}
