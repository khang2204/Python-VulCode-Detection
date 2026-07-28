def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
count = self.object_list.count()
context['count'] = count
return context
