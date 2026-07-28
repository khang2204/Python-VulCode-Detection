def validate(raw_schema, target=None, **kwargs):...
"""docstring"""
schema = schema_validator(raw_schema, **kwargs)
if target is not None:
validate_object(target, schema=schema, **kwargs)
