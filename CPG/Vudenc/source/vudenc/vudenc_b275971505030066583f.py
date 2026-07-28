def get_columns():...
columns = [{'fieldname': 'territory', 'fieldtype': 'Link', 'label': _(
    'Territory'), 'options': 'Territory', 'width': 100}, {'fieldname':
    'item_group', 'fieldtype': 'Link', 'label': _('Item Group'), 'options':
    'Item Group', 'width': 150}, {'fieldname': 'item_name', 'fieldtype':
    'Link', 'options': 'Item', 'label': 'Item', 'width': 150}, {'fieldname':
    'item_name', 'fieldtype': 'Data', 'label': _('Item Name'), 'width': 150
    }, {'fieldname': 'customer', 'fieldtype': 'Link', 'label': _('Customer'
    ), 'options': 'Customer', 'width': 100}, {'fieldname':
    'last_order_date', 'fieldtype': 'Date', 'label': _('Last Order Date'),
    'width': 100}, {'fieldname': 'qty', 'fieldtype': 'Float', 'label': _(
    'Quantity'), 'width': 100}, {'fieldname': 'days_since_last_order',
    'fieldtype': 'Int', 'label': _('Days Since Last Order'), 'width': 100}]
return columns
