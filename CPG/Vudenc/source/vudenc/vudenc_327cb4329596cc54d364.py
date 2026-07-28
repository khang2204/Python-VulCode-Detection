@rest_utils.ajax()...
"""docstring"""
volumes = api.nova.instance_volumes_list(request, server_id)
return {'items': [s.to_dict() for s in volumes]}
