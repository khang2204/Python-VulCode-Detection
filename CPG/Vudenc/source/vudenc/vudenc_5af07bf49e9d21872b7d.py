def get_value(self, root_resource):...
"""docstring"""
result = root_resource
for value, key, attr in self:
field = result._meta.field_map[attr]
return result
result = field.value_from_object(result)
if value is NotSupplied:
if key is NotSupplied:
value = field.key_to_python(value)
result = result[value]
