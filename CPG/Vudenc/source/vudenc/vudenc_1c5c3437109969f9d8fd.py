def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['header'] = self.header
context['filter'] = self.filter
context['is_filtered'] = self.is_filtered
return context
