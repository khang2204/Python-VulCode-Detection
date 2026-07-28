def convert_to(self, to_resource, context=None, ignore_fields=None, **...
"""docstring"""
mapping = registration.get_mapping(self.__class__, to_resource)
ignore_fields = ignore_fields or []
ignore_fields.extend(mapping.exclude_fields)
self.full_clean(ignore_fields)
return mapping(self, context).convert(**field_values)
