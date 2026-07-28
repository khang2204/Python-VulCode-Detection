@rest_utils.ajax()...
"""docstring"""
groups = api.network.server_security_groups(request, server_id)
return {'items': [s.to_dict() for s in groups]}
