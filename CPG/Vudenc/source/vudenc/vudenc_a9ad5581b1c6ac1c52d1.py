def insert_historic_cost(self, vendor_ref, min_qty, cost, vendors_code, date):...
"""docstring"""
vendor_id = self.get_vendor_id(vendor_ref)
supplierinfo = {'name': vendor_id.id, 'min_qty': min_qty, 'price': cost,
    'product_code': vendors_code, 'product_name': self.name, 'date_start':
    date, 'product_tmpl_id': self.id}
sellers = self.seller_ids.search([('name', '=', vendor_id.id), (
    'product_tmpl_id', '=', self.id), ('date_end', '=', False)])
for reg in sellers:
dt = datetime.strptime(date[0:10], '%Y-%m-%d')
self.seller_ids = [(0, 0, supplierinfo)]
dt = datetime.strftime(dt - timedelta(1), '%Y-%m-%d')
reg.date_end = dt if dt >= reg.date_start else reg.date_start
