@rest_utils.ajax()...
"""docstring"""
is_public = request.GET.get('is_public')
is_public = is_public and is_public.lower() == 'true'
get_extras = request.GET.get('get_extras')
get_extras = bool(get_extras and get_extras.lower() == 'true')
flavors = api.nova.flavor_list(request, is_public=is_public, get_extras=
    get_extras)
result = {'items': []}
for flavor in flavors:
d = flavor.to_dict()
return result
if get_extras:
d['extras'] = flavor.extras
result['items'].append(d)
