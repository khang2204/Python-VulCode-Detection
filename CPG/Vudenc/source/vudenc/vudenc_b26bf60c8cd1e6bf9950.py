def get_queryset(self, request, pk):...
pk = self.kwargs['pk']
query = Event.objects.filter(Q(id__in=Hunt(id=pk).events.all())).order_by(
    '-publish_timestamp')
return query
