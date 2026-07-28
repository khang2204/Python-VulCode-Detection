@api.multi...
self._secure_save_data()
super(ResPartner, self).forget_me()
self.write({'church_id': False, 'church_unlinked': False, 'street3': False,
    'firstname': False, 'deathdate': False, 'geo_point': False,
    'partner_latitude': False, 'partner_longitude': False})
self.advocate_details_id.unlink()
self.survey_inputs.unlink()
self.env['mail.tracking.email'].search([('partner_id', '=', self.id)]).unlink()
self.env['auditlog.log'].search([('model_id.model', '=', 'res.partner'), (
    'res_id', '=', self.id)]).unlink()
self.env['partner.communication.job'].search([('partner_id', '=', self.id)]
    ).unlink()
self.message_ids.unlink()
return True
