@api.multi...
partner_wizard = self.env['res.partner.check.double'].create({'partner_id':
    self.id})
return {'type': 'ir.actions.act_window', 'res_model':
    'res.partner.check.double', 'res_id': partner_wizard.id, 'view_type':
    'form', 'view_mode': 'form', 'target': 'new'}
