@rest_utils.ajax(data_required=True)...
"""docstring"""
if api.base.is_service_enabled(request, 'compute'):
disabled_quotas = quotas.get_disabled_quotas(request)
filtered_quotas = [quota for quota in quotas.NOVA_QUOTA_FIELDS if quota not in
    disabled_quotas]
request_data = {key: request.DATA.get(key, None) for key in filtered_quotas}
nova_data = {key: value for key, value in request_data.items() if value is not
    None}
api.nova.default_quota_update(request, **nova_data)
