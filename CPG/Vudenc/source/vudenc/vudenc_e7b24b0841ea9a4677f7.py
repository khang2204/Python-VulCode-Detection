def enterprise_fields_only(fields):...
"""docstring"""
enterprise_exclusions = configuration_helpers.get_value(
    'ENTERPRISE_EXCLUDED_REGISTRATION_FIELDS', settings.
    ENTERPRISE_EXCLUDED_REGISTRATION_FIELDS)
return [field for field in fields['fields'] if field['name'] not in
    enterprise_exclusions]
