def get_queryset(self):...
data = QueryDict('', mutable=True)
data.update(self.filter_data)
data.update(self.request.GET)
self.is_filtered = False
if len([k for k in data.keys() if k != 'page']) > 0:
self.is_filtered = True
self.filter = ConceptFilter(data)
self.queryset = self.filter.qs.select_related('transaction').prefetch_related(
    'value__currency').order_by('-id')
return self.queryset
