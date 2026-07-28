@api.multi...
"""docstring"""
res = super(ResPartner, self).onchange_type(is_company)
if is_company:
res['value']['title'] = self.env.ref(
    'partner_compassion.res_partner_title_friends').id
return res
