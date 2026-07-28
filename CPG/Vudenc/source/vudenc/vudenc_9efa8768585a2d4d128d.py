@api.model...
"""docstring"""
email = vals.get('email')
if email:
vals['email'] = email.strip()
duplicate = self.search(['|', '&', ('email', '=', vals.get('email')), (
    'email', '!=', False), '&', '&', ('firstname', 'ilike', vals.get(
    'firstname')), ('lastname', 'ilike', vals.get('lastname')), ('zip', '=',
    vals.get('zip'))])
duplicate_ids = [(4, itm.id) for itm in duplicate]
vals.update({'partner_duplicate_ids': duplicate_ids})
vals['ref'] = self.env['ir.sequence'].get('partner.ref')
partner = super(ResPartner, self.with_context(mail_create_nosubscribe=True)
    ).create(vals)
partner.compute_geopoint()
if partner.contact_type == 'attached' and not vals.get('active'):
partner.active = False
return partner
