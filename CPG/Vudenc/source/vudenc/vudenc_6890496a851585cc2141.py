@rest_utils.ajax()...
"""docstring"""
result = api.nova.server_group_list(request)
return {'items': [u.to_dict() for u in result]}
