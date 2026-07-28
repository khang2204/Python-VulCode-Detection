def get_queryset(self, request):...
query = Hunt.objects.order_by('id')
query = query.annotate(count=Count('tweet'))
return query
