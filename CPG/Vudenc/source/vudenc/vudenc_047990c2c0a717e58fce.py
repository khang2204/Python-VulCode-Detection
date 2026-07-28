def get_queryset(self):...
query = Hunt.objects.order_by('id')
query = query.annotate(count=Count('events'))
return query
