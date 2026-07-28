@rest_utils.ajax()...
"""docstring"""
disabled_quotas = quotas.get_disabled_quotas(request)
editable_quotas = [quota for quota in quotas.QUOTA_FIELDS if quota not in
    disabled_quotas]
return {'items': editable_quotas}
