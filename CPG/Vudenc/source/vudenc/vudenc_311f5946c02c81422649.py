@rest_utils.ajax(data_required=True)...
instance_id = request.DATA['instance_id']
name = request.DATA['name']
result = api.nova.snapshot_create(request, instance_id=instance_id, name=name)
return result
