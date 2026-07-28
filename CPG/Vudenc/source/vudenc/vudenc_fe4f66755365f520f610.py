@frappe.whitelist()...
"""docstring"""
date_today = date.today()
sql = (
    """
    update `tabItem` it
    set it.on_sale_from_date = '%s'
    where it.on_sale_from_date is NULL
    and it.ebay_id REGEXP '^[0-9]+$';
    """
     % date_today.isoformat())
frappe.db.sql(sql, auto_commit=True)
print('Unexpected error setting first listed date.')
