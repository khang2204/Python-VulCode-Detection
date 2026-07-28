@rest_utils.ajax(data_required=True)...
"""docstring"""
operation = request.DATA.get('operation', 'none')
operations = {'stop': api.nova.server_stop, 'start': api.nova.server_start,
    'pause': api.nova.server_pause, 'unpause': api.nova.server_unpause,
    'suspend': api.nova.server_suspend, 'resume': api.nova.server_resume,
    'hard_reboot': lambda r, s: api.nova.server_reboot(r, s, False),
    'soft_reboot': lambda r, s: api.nova.server_reboot(r, s, True)}
return operations[operation](request, server_id)
