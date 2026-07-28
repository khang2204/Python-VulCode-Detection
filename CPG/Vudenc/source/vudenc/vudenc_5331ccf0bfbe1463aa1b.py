def get_queryset(self):...
data = QueryDict('', mutable=True)
data.update(self.filter_data)
data.update(self.request.GET)
self.is_filtered = False
if len([k for k in data.keys() if k != 'page']) > 0:
self.is_filtered = True
self.filter = TransactionFilter(data)
self.queryset = self.filter.qs.select_related('cashclose').prefetch_related(
    'concepts__value__currency').order_by('-id')
return self.queryset
