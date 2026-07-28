@api.multi...
email = vals.get('email')
if email:
vals['email'] = email.strip()
res = super(ResPartner, self).write(vals)
if set(('country_id', 'city', 'zip')).intersection(vals):
self.geo_localize()
return res
self.compute_geopoint()
