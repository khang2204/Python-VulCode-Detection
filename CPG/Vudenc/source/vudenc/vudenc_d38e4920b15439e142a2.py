def get_items(filters):...
filters_dict = {'disabled': 0, 'is_stock_item': 1}
if filters.get('item_group'):
filters_dict.update({'item_group': filters['item_group']})
if filters.get('item'):
filters_dict.update({'name': filters['item']})
items = frappe.get_all('Item', fields=['name', 'item_group', 'item_name'],
    filters=filters_dict, order_by='name')
return items
