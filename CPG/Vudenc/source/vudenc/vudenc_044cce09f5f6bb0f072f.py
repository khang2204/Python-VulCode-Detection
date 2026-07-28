def get_context_data(self, **kwargs):...
pk = self.kwargs['pk']
event_obj = Event.objects.get(pk=pk)
objects_obj = Object.objects.filter(event=pk)
context = super().get_context_data(**kwargs)
context['event'] = event_obj
context['objects'] = objects_obj
context['categories'] = event_obj.getUniqCategory()
context['types'] = event_obj.getUniqType()
context['count'] = self.object_list.count()
return context
