def sync_ebay_ids():...
"""docstring"""
sql = """
    select * from (
        SELECT t1.sku, t2.item_code, ifnull(t1.ebay_id, '') as live_ebay_id,
        ifnull(t2.ebay_id, '') as dead_ebay_id FROM `zEbayListings` t1
        LEFT JOIN `tabItem` t2 ON t1.sku = t2.item_code
        UNION
        SELECT t1.sku, t2.item_code, ifnull(t1.ebay_id, '') as live_ebay_id,
        ifnull(t2.ebay_id, '') as dead_ebay_id FROM `zEbayListings` t1
        RIGHT JOIN `tabItem` t2 ON t1.sku = t2.item_code
    ) as t
    where t.live_ebay_id <> t.dead_ebay_id
    """
records = frappe.db.sql(sql, as_dict=True)
for r in records:
if r.live_ebay_id == '':
set_item_ebay_id(r.item_code, '')
if r.item_code:
set_item_ebay_id(r.sku, r.live_ebay_id)
msgprint('The ebay item cannot be found on ERPNEXT so unable to record ebay id'
    , r.live_ebay_id)
