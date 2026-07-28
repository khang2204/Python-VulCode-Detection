@rest_utils.ajax(data_required=True)...
flavor_access = request.DATA.get('flavor_access', [])
is_public = not flavor_access
extras_dict = api.nova.flavor_get_extras(request, flavor_id, raw=True)
api.nova.flavor_delete(request, flavor_id)
flavor = api.nova.flavor_create(request, name=request.DATA['name'], memory=
    request.DATA['ram'], vcpu=request.DATA['vcpus'], disk=request.DATA[
    'disk'], ephemeral=request.DATA['OS-FLV-EXT-DATA:ephemeral'], swap=
    request.DATA['swap'], flavorid=flavor_id, is_public=is_public)
for project in flavor_access:
api.nova.add_tenant_to_flavor(request, flavor.id, project.get('id'))
if extras_dict:
api.nova.flavor_extra_set(request, flavor.id, extras_dict)
