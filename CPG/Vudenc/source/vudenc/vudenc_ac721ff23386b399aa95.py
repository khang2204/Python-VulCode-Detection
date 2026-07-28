def onchange_partner_id(self, cr, uid, ids, part):...
if not part:
return {'value': {'contact_id': False, 'pricelist_id': False}}
addr = self.pool.get('res.partner').address_get(cr, uid, [part], ['contact'])
pricelist = self.pool.get('res.partner').browse(cr, uid, part
    ).property_product_pricelist.id
return {'value': {'contact_id': addr['contact'], 'pricelist_id': pricelist}}
