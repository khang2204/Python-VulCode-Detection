@rest_utils.ajax(json_encoder=json_encoder.NaNJSONEncoder)...
"""docstring"""
reserved = request.GET.get('reserved') == 'true'
result = api.nova.tenant_absolute_limits(request, reserved)
return result
