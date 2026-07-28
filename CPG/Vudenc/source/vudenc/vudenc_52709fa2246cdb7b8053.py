def get(self, request):...
self.object_list = self.get_queryset(request)
context = self.get_context_data()
return render(request, 'twitter_hunter/index.html', context)
