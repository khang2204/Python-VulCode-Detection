@rest_utils.ajax()...
"""docstring"""
log_length = request.DATA.get('length', 100)
console_lines = api.nova.server_console_output(request, server_id,
    tail_length=log_length)
return {'lines': [x for x in console_lines.split('\n')]}
