def get_queryset(self):...
query = Attribute.objects.order_by('-timestamp')
category = self.request.GET.get('category')
type = self.request.GET.get('type')
if category is not None:
query = query.filter(category=category)
if type is not None:
query = query.filter(type=type)
keyword = self.request.GET.get('keyword')
if keyword is not None:
query = query.filter(Q(value__icontains=keyword)).order_by('-timestamp')
return query
