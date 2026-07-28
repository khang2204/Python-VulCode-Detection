@rest_utils.ajax()...
"""docstring"""
updated = request.DATA['updated']
removed = request.DATA['removed']
if updated:
api.nova.server_metadata_update(request, server_id, updated)
if removed:
api.nova.server_metadata_delete(request, server_id, removed)
