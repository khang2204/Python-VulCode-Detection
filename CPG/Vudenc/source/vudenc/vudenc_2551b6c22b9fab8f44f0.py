@frappe.whitelist()...
"""docstring"""
create_ebay_listings_table()
page = 1
listings_dict = get_myebay_selling_request(page)
pages = int(listings_dict['ActiveList']['PaginationResult'][
    'TotalNumberOfPages'])
while pages >= page:
for item in listings_dict['ActiveList']['ItemArray']['Item']:
ebay_id = item['ItemID']
page += 1
qty = int(item['QuantityAvailable'])
if pages >= page:
sku = item['SKU']
sku = ''
curr_ebay_price = float(item['SellingStatus']['CurrentPrice']['value'])
listings_dict = get_myebay_selling_request(page)
curr_ex_vat = curr_ebay_price / ugssettings.VAT
hit_count = 0
watch_count = 0
question_count = 0
site = ''
insert_ebay_listing(sku, ebay_id, qty, curr_ebay_price, site, hit_count,
    watch_count, question_count)
