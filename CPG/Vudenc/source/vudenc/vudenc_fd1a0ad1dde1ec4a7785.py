def build_filter_conditions(self, filters, conditions, ignore_permissions=None...
"""docstring"""
if ignore_permissions is not None:
self.flags.ignore_permissions = ignore_permissions
if isinstance(filters, dict):
filters = [filters]
for f in filters:
if isinstance(f, string_types):
conditions.append(f)
conditions.append(self.prepare_filter_condition(f))
