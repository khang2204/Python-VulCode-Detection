def parse_args(self):...
"""docstring"""
if isinstance(self.fields, string_types):
if self.fields == '*':
for filter_name in ['filters', 'or_filters']:
self.fields = ['*']
self.fields = json.loads(self.fields)
self.fields = [f.strip() for f in self.fields.split(',')]
filters = getattr(self, filter_name)
if isinstance(filters, string_types):
filters = json.loads(filters)
if isinstance(filters, dict):
fdict = filters
setattr(self, filter_name, filters)
filters = []
for key, value in iteritems(fdict):
filters.append(make_filter_tuple(self.doctype, key, value))
