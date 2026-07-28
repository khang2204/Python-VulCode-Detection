@api.multi...
"""docstring"""
self.filtered(lambda p: not p.partner_latitude or not p.partner_longitude
    ).geo_localize()
for partner in self.filtered(lambda p: p.partner_latitude and p.
geo_point = GeoPoint.from_latlon(self.env.cr, partner.partner_latitude,
    partner.partner_longitude)
return True
vals = {'geo_point': geo_point.wkt}
partner.write(vals)
partner.advocate_details_id.write(vals)
