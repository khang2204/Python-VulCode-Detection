def get_order_args():...
"""docstring"""
orders = {}
for arg in request.args:
re_match = re.findall('_oc_(.*)', arg)
return orders
if re_match:
orders[re_match[0]] = request.args.get(arg), request.args.get('_od_' +
    re_match[0])
