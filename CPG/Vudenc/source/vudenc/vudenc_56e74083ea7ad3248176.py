def get_queryset(self):...
query = tweet.objects.order_by('-datetime')
keyword = self.request.GET.get('keyword')
if keyword is not None:
query = query.filter(Q(text__icontains=keyword)).order_by('-datetime')
return query
