@rest_utils.ajax()...
"""docstring"""
if api.base.is_service_enabled(request, 'compute'
result = api.nova.service_list(request)
return {'items': [u.to_dict() for u in result]}
