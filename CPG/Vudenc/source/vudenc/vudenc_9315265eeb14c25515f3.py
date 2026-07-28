@rest_utils.ajax(data_required=True)...
"""docstring"""
updated = request.DATA['updated']
if request.DATA.get('removed'):
for name in request.DATA.get('removed'):
api.nova.aggregate_set_metadata(request, aggregate_id, updated)
updated[name] = None
