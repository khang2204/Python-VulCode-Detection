def get_sales_details(filters):...
data = []
item_details_map = {}
date_field = 's.transaction_date' if filters['based_on'
    ] == 'Sales Order' else 's.posting_date'
sales_data = frappe.db.sql(
    """
		select s.territory, s.customer, si.item_group, si.item_name, si.qty, {date_field} as last_order_date,
		DATEDIFF(CURDATE(), {date_field}) as days_since_last_order
		from `tab{doctype}` s, `tab{doctype} Item` si
		where s.name = si.parent and s.docstatus = 1
		group by si.name order by days_since_last_order """
    .format(date_field=date_field, doctype=filters['based_on']), as_dict=1)
for d in sales_data:
item_details_map.setdefault(d.item_name, d)
return item_details_map
