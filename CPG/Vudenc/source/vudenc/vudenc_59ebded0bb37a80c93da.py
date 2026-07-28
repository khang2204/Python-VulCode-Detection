def set_item_ebay_id(item_code, ebay_id):...
"""docstring"""
if ebay_id == '':
sql = (
    """update `tabItem` it
            set it.ebay_id = '{}'
            where it.item_code = '{}' 
            and it.ebay_id <> '{}'
            """
    .format(ebay_id, item_code, 'Awaiting Garagesale'))
sql = (
    """update `tabItem` it
            set it.ebay_id = '{}'
            where it.item_code = '{}' 
            """
    .format(ebay_id, item_code))
frappe.db.sql(sql, auto_commit=True)
print('Unexpected error running ebay_id sync.', item_code)
return True
