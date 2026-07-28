def get(self, request, pk):...
self.object_list = self.get_queryset(request, pk)
context = self.get_context_data()
return render(request, 'threat_hunter/event_list.html', context)
