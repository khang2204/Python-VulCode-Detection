@rest_utils.ajax(data_required=True)...
"""docstring"""
if 'public_key' in request.DATA:
new = api.nova.keypair_import(request, request.DATA['name'], request.DATA[
    'public_key'])
new = api.nova.keypair_create(request, request.DATA['name'])
return rest_utils.CreatedResponse('/api/nova/keypairs/%s' % utils_http.
    urlquote(new.name), new.to_dict())
