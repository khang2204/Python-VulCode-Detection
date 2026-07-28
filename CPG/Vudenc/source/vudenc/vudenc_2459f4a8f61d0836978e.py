def get_columns(self):...
"""docstring"""
if not self.list_display:
return [SmartColumn(self.model, '__str__', 1, self.ordering_query_value,
    self.ordering_query_param)]
columns = []
for index, field in enumerate(self.list_display, start=1):
kwargs = {'model': self.model, 'column_id': index, 'query_params': self.
    query_params, 'ordering_query_param': self.ordering_query_param}
return columns
field, label = field
kwargs['field'] = field
if callable(field):
columns.append(SmartColumn(**kwargs))
kwargs['field'], kwargs['render_function'], kwargs['label'
    ] = None, field, label
kwargs['field'], kwargs['label'] = field, label
