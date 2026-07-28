@rest_utils.ajax(data_required=True)...
"""docstring"""
disabled_quotas = quotas.get_disabled_quotas(request)
if api.base.is_service_enabled(request, 'compute'):
nova_data = {key: request.DATA[key] for key in quotas.NOVA_QUOTA_FIELDS if 
    key not in disabled_quotas}
api.nova.tenant_quota_update(request, project_id, **nova_data)
