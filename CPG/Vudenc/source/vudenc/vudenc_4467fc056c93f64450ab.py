def get_prep_lookup(self):...
values = super().get_prep_lookup()
if hasattr(values, 'resolve_expression'):
return values
prepared_values = []
for value in values:
if hasattr(value, 'resolve_expression'):
return prepared_values
prepared_values.append(value)
prepared_values.append(tuple(value))
