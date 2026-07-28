@rest_utils.ajax()...
"""docstring"""
if api.base.is_service_enabled(request, 'compute'):
quota_set = api.nova.default_quota_get(request, request.user.tenant_id)
disabled_quotas = quotas.get_disabled_quotas(request)
filtered_quotas = [quota for quota in quota_set if quota.name not in
    disabled_quotas]
result = [{'display_name': quotas.QUOTA_NAMES.get(quota.name, quota.name.
    replace('_', ' ').title()) + '', 'name': quota.name, 'limit': quota.
    limit} for quota in filtered_quotas]
return {'items': result}
