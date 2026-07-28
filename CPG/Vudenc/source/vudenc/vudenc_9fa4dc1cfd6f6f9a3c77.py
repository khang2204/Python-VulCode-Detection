@rest_utils.ajax()...
"""docstring"""
actions = api.nova.instance_action_list(request, server_id)
return {'items': [s.to_dict() for s in actions]}
