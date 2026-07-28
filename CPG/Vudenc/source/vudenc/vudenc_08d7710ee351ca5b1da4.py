@rest_utils.ajax()...
"""docstring"""
servers = api.nova.server_list(request)[0]
return {'items': [s.to_dict() for s in servers]}
