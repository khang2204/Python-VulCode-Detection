def get_vendor_id(self, vendor_ref):...
vendor_id = self.env['res.partner'].search([('ref', '=', vendor_ref)])
if not vendor_id:
return vendor_id
