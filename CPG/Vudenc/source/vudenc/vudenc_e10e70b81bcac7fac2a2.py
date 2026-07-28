@rest_utils.ajax(data_required=True)...
"""docstring"""
args = request, request.DATA['name'], request.DATA['source_id'], request.DATA[
    'flavor_id'], request.DATA['key_name'], request.DATA['user_data'
    ], request.DATA['security_groups']
kw = {}
for name in self._optional_create:
if name in request.DATA:
new = api.nova.server_create(*args, **kw)
kw[name] = request.DATA[name]
return rest_utils.CreatedResponse('/api/nova/servers/%s' % utils_http.
    urlquote(new.id), new.to_dict())
