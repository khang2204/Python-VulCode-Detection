def get_data(filters):...
data = []
items = get_items(filters)
sales_invoice_data = get_sales_details(filters)
for item in items:
if sales_invoice_data.get(item.name):
return data
item_obj = sales_invoice_data[item.name]
row = {'item_group': item.item_group, 'item': item.name, 'item_name': item.
    item_name}
if item_obj.days_since_last_order > cint(filters['days']):
data.append(row)
row = {'territory': item_obj.territory, 'item_group': item_obj.item_group,
    'item': item_obj.name, 'item_name': item_obj.item_name, 'customer':
    item_obj.customer, 'last_order_date': item_obj.last_order_date, 'qty':
    item_obj.qty, 'days_since_last_order': item_obj.days_since_last_order}
data.append(row)
