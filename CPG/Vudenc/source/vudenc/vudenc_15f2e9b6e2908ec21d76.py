@rest_utils.ajax()...
"""docstring"""
detailed = request.GET.get('detailed') == 'true'
result = api.nova.availability_zone_list(request, detailed)
return {'items': [u.to_dict() for u in result]}
