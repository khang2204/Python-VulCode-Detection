@rest_utils.ajax()...
"""docstring"""
result = api.nova.list_extensions(request)
return {'items': [e.to_dict() for e in result]}
