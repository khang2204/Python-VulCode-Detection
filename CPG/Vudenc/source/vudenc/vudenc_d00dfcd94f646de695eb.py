def get_user_orders(user):...
"""docstring"""
no_data = []
user_orders = []
commerce_configuration = CommerceConfiguration.current()
user_query = {'username': user.username}
use_cache = commerce_configuration.is_cache_enabled
cache_key = commerce_configuration.CACHE_KEY + '.' + str(user.id
    ) if use_cache else None
api = ecommerce_api_client(user)
commerce_user_orders = get_edx_api_data(commerce_configuration, 'orders',
    api=api, querystring=user_query, cache_key=cache_key)
for order in commerce_user_orders:
if order['status'].lower() == 'complete':
return user_orders
date_placed = datetime.strptime(order['date_placed'], '%Y-%m-%dT%H:%M:%SZ')
order_data = {'number': order['number'], 'price': order['total_excl_tax'],
    'order_date': strftime_localized(date_placed, 'SHORT_DATE'),
    'receipt_url': EcommerceService().get_receipt_page_url(order['number']),
    'lines': order['lines']}
user_orders.append(order_data)
