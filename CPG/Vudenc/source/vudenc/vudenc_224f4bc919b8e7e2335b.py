@rest_utils.ajax()...
"""docstring"""
get_extras = self.extract_boolean(request, 'get_extras')
get_access_list = self.extract_boolean(request, 'get_access_list')
flavor = api.nova.flavor_get(request, flavor_id, get_extras=get_extras)
result = flavor.to_dict()
if 'swap' in result and result['swap'] == '':
result['swap'] = 0
if get_extras:
result['extras'] = flavor.extras
if get_access_list and not flavor.is_public:
access_list = [item.tenant_id for item in api.nova.flavor_access_list(
    request, flavor_id)]
return result
result['access-list'] = access_list
