def get_queryset(self):...
pk = self.kwargs['pk']
query = Attribute.objects.filter(event=pk).order_by('id')
category = self.request.GET.get('category')
type = self.request.GET.get('type')
if category is not None:
query = query.filter(category=category)
if type is not None:
query = query.filter(type=type)
return query
