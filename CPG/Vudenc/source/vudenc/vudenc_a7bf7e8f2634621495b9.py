@rest_utils.ajax(data_required=True)...
"""docstring"""
if request.DATA.get('removed'):
api.nova.flavor_extra_delete(request, flavor_id, request.DATA.get('removed'))
api.nova.flavor_extra_set(request, flavor_id, request.DATA['updated'])
