@api.multi...
"""docstring"""
return super(ResPartner, self + self.mapped('church_id')
    ).update_number_sponsorships()
