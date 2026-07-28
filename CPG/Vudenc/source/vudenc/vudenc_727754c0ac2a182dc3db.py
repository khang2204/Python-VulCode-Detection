def _get_active_sponsorships_domain(self):...
"""docstring"""
domain = super(ResPartner, self)._get_active_sponsorships_domain()
domain.insert(0, '|')
domain.insert(3, ('partner_id', 'in', self.mapped('member_ids').ids))
domain.insert(4, '|')
domain.insert(6, ('correspondent_id', 'in', self.mapped('member_ids').ids))
return domain
